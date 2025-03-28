import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from font_styles import transform_text, FONT_STYLES
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    try:
        await update.message.reply_text(
            "Send me any text and I'll style it for you! 🎨\n\nI have lots of beautiful styles to choose from! ✨"
        )
    except Exception as e:
        logger.error(f"Error in start command: {e}")

async def style_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages and show style options."""
    try:
        text = update.message.text
        keyboard = []
        current_row = []
        
        # Create buttons for each style, 4 buttons per row
        for i, style_name in enumerate(FONT_STYLES.keys(), 1):
            current_row.append(InlineKeyboardButton(
                style_name, 
                callback_data=f"{style_name}|{text}"
            ))
            
            if len(current_row) == 4:  # Changed from 2 to 4 buttons per row
                keyboard.append(current_row)
                current_row = []
        
        # Add any remaining buttons
        if current_row:
            keyboard.append(current_row)
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            '✨ Choose a style for your text:\n\n' + 
            'I have many beautiful styles! Click any button to see the magic! 🎨',
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"Error in style_text: {e}")
        await update.message.reply_text("Sorry, something went wrong. Please try again.")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    try:
        query = update.callback_query
        await query.answer()
        
        # Extract style and text from callback data
        style_name, text = query.data.split('|', 1)
        
        # Transform text using selected style
        styled_text = transform_text(text, style_name)
        
        # Send as new message instead of editing
        await query.message.reply_text(
            f"{styled_text}\n\n✨ Send another text to style it differently! ✨"
        )
    except Exception as e:
        logger.error(f"Error in button_callback: {e}")
        await query.message.reply_text("Sorry, something went wrong. Please try again.")

def main() -> None:
    """Start the bot."""
    try:
        # Create the Application
        token = '7865807991:AAHvNNJYDi84o1dcnqwaxlH0mQmr5Fiysa8'
        application = Application.builder().token(token).build()

        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, style_text))
        application.add_handler(CallbackQueryHandler(button_callback))

        # Start the Bot
        logger.info("Bot is starting...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"Error in main: {e}")

if __name__ == '__main__':
    main() 