import os
import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from dotenv import load_dotenv
from name_fonts import style_name, NORMAL_FONTS, FANCY_FONTS, STYLE_MAPS
from aiohttp import web

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Store user states
user_states = {}

# Get port from environment variable or use default
PORT = int(os.getenv("PORT", "8080"))

# Get service name from environment
SERVICE_NAME = os.getenv("RENDER_SERVICE_NAME")
if not SERVICE_NAME:
    logger.error("RENDER_SERVICE_NAME not found in environment variables!")
    exit(1)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors."""
    logger.error(f"Error: {context.error}")
    try:
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "Sorry, something went wrong. Please try sending your name again and then use the style commands."
            )
    except Exception as e:
        logger.error(f"Error in error handler: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    try:
        await update.message.reply_text(
            "👋 Welcome to the Name Style Bot!\n\n"
            "1️⃣ Send me your name\n"
            "2️⃣ Then use these commands:\n"
            "   /text - Text font styles\n"
            "   /fancy - Fancy name designs\n"
            "   /font - Simple decorations\n\n"
            "You can also use commands directly with your name:\n"
            "Example: /text YourName"
        )
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        await update.message.reply_text("Sorry, something went wrong. Please try again.")

async def show_style_options(update: Update, context: ContextTypes.DEFAULT_TYPE, style_type: str) -> None:
    """Show style options for the given type."""
    try:
        message_text = update.message.text.split()
        if len(message_text) > 1:
            name = " ".join(message_text[1:])
            user_states[update.effective_user.id] = name
            logger.info(f"Name set from command: {name}")
        else:
            name = user_states.get(update.effective_user.id)
            logger.info(f"Name retrieved from state: {name}")
        
        if not name:
            await update.message.reply_text(
                "Please send me your name first!\n"
                f"Or use: {message_text[0]} YourName"
            )
            return

        examples_text = f"Choose a style number for '{name}':\n\n"
        styles_dict = {
            "text": STYLE_MAPS,
            "normal": NORMAL_FONTS,
            "fancy": FANCY_FONTS
        }.get(style_type)
            
        if not styles_dict:
            logger.error(f"No styles found for type: {style_type}")
            await update.message.reply_text("Sorry, no styles available right now. Please try again later.")
            return
            
        keyboard = []
        row = []
        
        for i, style_key in enumerate(styles_dict.keys(), 1):
            try:
                styled_name = style_name(name, style_type, style_key)
                examples_text += f"{i}. {styled_name}\n"
                
                callback_data = f"{style_type}|{style_key}"
                row.append(InlineKeyboardButton(str(i), callback_data=callback_data))
                
                if len(row) == 3:  # 3 buttons per row
                    keyboard.append(row)
                    row = []
            except Exception as e:
                logger.error(f"Error creating style example {i}: {e}")
                continue
                
        if row:  # Add any remaining buttons
            keyboard.append(row)
            
        if not keyboard:
            await update.message.reply_text("Sorry, couldn't create style options. Please try again.")
            return
            
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(examples_text, reply_markup=reply_markup)
        
    except Exception as e:
        logger.error(f"Error in show_style_options: {e}")
        await update.message.reply_text(
            "Sorry, something went wrong. Please try again or send your name first."
        )

async def text_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /text command."""
    await show_style_options(update, context, "text")

async def fancy_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /fancy command."""
    await show_style_options(update, context, "fancy")

async def font_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /font command."""
    await show_style_options(update, context, "normal")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages."""
    try:
        name = update.message.text.strip()
        if len(name) > 50:
            await update.message.reply_text("Please send a shorter name (maximum 50 characters).")
            return

        user_states[update.effective_user.id] = name
        await update.message.reply_text(
            f"Great! I'll style '{name}' for you.\n"
            "Choose a style command:\n"
            "/text - Text font styles\n"
            "/fancy - Fancy name designs\n"
            "/font - Simple decorations"
        )
    except Exception as e:
        logger.error(f"Error in handle_text: {e}")
        await update.message.reply_text("Sorry, something went wrong. Please try again.")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    try:
        query = update.callback_query
        await query.answer()
        
        style_type, style_key = query.data.split("|")
        name = user_states.get(query.from_user.id)
        
        if not name:
            await query.message.reply_text("Please send me your name first!")
            return
        
        logger.info(f"Styling name: {name} with type: {style_type} and style: {style_key}")
        styled_name = style_name(name, style_type, style_key)
        
        if styled_name and styled_name != name:
            await query.message.reply_text(
                f"Here's your styled name:\n\n{styled_name}\n\n"
                f"Use /{style_type} command to try more styles!"
            )
        else:
            logger.error(f"Style failed for {name} with {style_type}|{style_key}")
            await query.message.reply_text(
                "Sorry, couldn't apply this style. Please try another one."
            )
    except Exception as e:
        logger.error(f"Error in button handler: {e}")
        await query.message.reply_text("Sorry, something went wrong. Please try again.")

async def health_check(request):
    """Handle health check requests."""
    return web.Response(text="OK")

async def webhook_handler(request):
    """Handle incoming webhook requests."""
    try:
        data = await request.json()
        update = Update.de_json(data, request.app.bot)
        await request.app.application.process_update(update)
        return web.Response()
    except Exception as e:
        logger.error(f"Error in webhook handler: {e}")
        return web.Response(status=500)

async def main():
    """Start the bot."""
    # Get bot token from environment variable
    token = os.getenv("BOT_TOKEN")
    if not token:
        logger.error("No bot token found in environment variables!")
        return

    # Create application
    app = Application.builder().token(token).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("text", text_command))
    app.add_handler(CommandHandler("fancy", fancy_command))
    app.add_handler(CommandHandler("font", font_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(CallbackQueryHandler(button))
    
    # Add error handler
    app.add_error_handler(error_handler)

    # Create web application
    web_app = web.Application()
    web_app.bot = app.bot
    web_app.application = app

    # Add routes
    web_app.router.add_get('/', health_check)  # Root path for health check
    web_app.router.add_get('/health', health_check)
    web_app.router.add_post('/webhook', webhook_handler)

    # Start web server first
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()
    logger.info(f"Web server started on port {PORT}")

    # Set webhook
    webhook_url = f"https://{SERVICE_NAME}.onrender.com/webhook"
    await app.bot.set_webhook(url=webhook_url)
    logger.info(f"Webhook set to: {webhook_url}")

    # Start the bot without polling
    logger.info("Starting bot with webhooks...")
    await app.initialize()
    await app.start()

    # Keep the bot running
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Critical error in main: {e}") 