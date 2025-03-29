import os
import logging
import asyncio
from typing import Optional, Dict
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
    ApplicationBuilder
)
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

class NameStyleBot:
    def __init__(self):
        self.user_states: Dict[int, str] = {}
        self.application: Optional[Application] = None
        self.token = os.getenv("BOT_TOKEN")
        
        if not self.token:
            raise ValueError("No bot token found in environment variables!")

    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle errors."""
        logger.error(f"Error: {context.error}")
        try:
            if update and update.effective_message:
                await update.effective_message.reply_text(
                    "Sorry, something went wrong. Please try sending your name again and then use the style commands."
                )
        except Exception as e:
            logger.error(f"Error in error handler: {e}")

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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

    async def show_style_options(self, update: Update, context: ContextTypes.DEFAULT_TYPE, style_type: str) -> None:
        """Show style options for the given type."""
        try:
            message_text = update.message.text.split()
            if len(message_text) > 1:
                name = " ".join(message_text[1:])
                self.user_states[update.effective_user.id] = name
                logger.info(f"Name set from command: {name}")
            else:
                name = self.user_states.get(update.effective_user.id)
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

    async def text_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /text command."""
        await self.show_style_options(update, context, "text")

    async def fancy_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /fancy command."""
        await self.show_style_options(update, context, "fancy")

    async def font_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /font command."""
        await self.show_style_options(update, context, "normal")

    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle text messages."""
        try:
            name = update.message.text.strip()
            if len(name) > 50:
                await update.message.reply_text("Please send a shorter name (maximum 50 characters).")
                return

            self.user_states[update.effective_user.id] = name
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

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle button presses."""
        try:
            query = update.callback_query
            await query.answer()
            
            style_type, style_key = query.data.split("|")
            name = self.user_states.get(query.from_user.id)
            
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

    async def setup(self) -> None:
        """Setup the bot application."""
        self.application = ApplicationBuilder().token(self.token).build()

        # Add handlers
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("text", self.text_command))
        self.application.add_handler(CommandHandler("fancy", self.fancy_command))
        self.application.add_handler(CommandHandler("font", self.font_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text))
        self.application.add_handler(CallbackQueryHandler(self.button))
        
        # Add error handler
        self.application.add_error_handler(self.error_handler)

    async def start_bot(self) -> None:
        """Start the bot."""
        try:
            await self.setup()
            logger.info("Starting bot...")
            await self.application.initialize()
            await self.application.start()
            await self.application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
        except Exception as e:
            logger.error(f"Critical error in start_bot: {e}")
            if self.application:
                try:
                    await self.application.stop()
                except Exception as stop_error:
                    logger.error(f"Error stopping application: {stop_error}")

def run_bot():
    """Run the bot with proper event loop handling."""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")

async def main() -> None:
    """Main function to run the bot."""
    bot = NameStyleBot()
    try:
        await bot.start_bot()
    except Exception as e:
        logger.error(f"Fatal error: {e}")

if __name__ == '__main__':
    run_bot() 