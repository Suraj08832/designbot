import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from dotenv import load_dotenv
from name_fonts import style_name, NORMAL_FONTS, FANCY_FONTS, STYLE_MAPS

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

def create_style_keyboard(style_type: str) -> InlineKeyboardMarkup:
    """Create keyboard with style options."""
    keyboard = []
    row = []
    
    if style_type == "text":
        styles = STYLE_MAPS
    elif style_type == "normal":
        styles = NORMAL_FONTS
    else:
        styles = FANCY_FONTS
    
    for i, style_name in enumerate(styles.keys(), 1):
        callback_data = f"{style_type}|{style_name}"
        row.append(InlineKeyboardButton(str(i), callback_data=callback_data))
        
        if len(row) == 3:  # 3 buttons per row
            keyboard.append(row)
            row = []
    
    if row:  # Add any remaining buttons
        keyboard.append(row)
    
    return InlineKeyboardMarkup(keyboard)

async def show_style_options(update: Update, context: ContextTypes.DEFAULT_TYPE, style_type: str) -> None:
    """Show style options for the given type."""
    try:
        # Check if name is provided in command
        message_text = update.message.text.split()
        if len(message_text) > 1:
            name = " ".join(message_text[1:])
            user_states[update.effective_user.id] = name
        else:
            name = user_states.get(update.effective_user.id)
        
        if not name:
            await update.message.reply_text(
                "Please send me your name first!\n"
                f"Or use: {message_text[0]} YourName"
            )
            return

        # Show style examples
        examples_text = "Choose a style number for your name:\n\n"
        if style_type == "text":
            styles = STYLE_MAPS
            for i, (style_key, _) in enumerate(styles.items(), 1):
                styled_name = style_name(name, "text", style_key)
                examples_text += f"{i}. {styled_name}\n"
        elif style_type == "normal":
            styles = NORMAL_FONTS
            for i, (style_name, pattern) in enumerate(styles.items(), 1):
                styled_name = pattern.replace("NAME", name)
                examples_text += f"{i}. {styled_name}\n"
        else:
            styles = FANCY_FONTS
            for i, (style_name, pattern) in enumerate(styles.items(), 1):
                styled_name = pattern.replace("NAME", name)
                examples_text += f"{i}. {styled_name}\n"

        keyboard = create_style_keyboard(style_type)
        await update.message.reply_text(examples_text, reply_markup=keyboard)
    except Exception as e:
        logger.error(f"Error in show_style_options: {e}")
        await update.message.reply_text("Sorry, something went wrong. Please try sending your name again.")

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
        
        try:
            styled_name = style_name(name, style_type, style_key)
            if styled_name:
                await query.message.reply_text(
                    f"Here's your styled name:\n\n{styled_name}\n\n"
                    f"Use /{style_type} command to try more styles!"
                )
            else:
                raise ValueError("Could not style the name")
        except Exception as style_error:
            logger.error(f"Error applying style: {style_error}")
            await query.message.reply_text(
                "Sorry, couldn't apply this style. Please try another one or send your name again."
            )
    except Exception as e:
        logger.error(f"Error in button handler: {e}")
        await query.message.reply_text("Sorry, something went wrong. Please try again.")

def main() -> None:
    """Start the bot."""
    try:
        # Get bot token from environment variable
        token = os.getenv("BOT_TOKEN")
        if not token:
            logger.error("No bot token found in environment variables!")
            return

        # Create application
        application = Application.builder().token(token).build()

        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("text", text_command))
        application.add_handler(CommandHandler("fancy", fancy_command))
        application.add_handler(CommandHandler("font", font_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
        application.add_handler(CallbackQueryHandler(button))
        
        # Add error handler
        application.add_error_handler(error_handler)

        # Start the bot
        logger.info("Starting bot...")
        application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
    except Exception as e:
        logger.error(f"Critical error in main: {e}")

if __name__ == '__main__':
    main() 