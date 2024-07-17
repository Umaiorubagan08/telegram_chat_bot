
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6345033528:AAGHRoIRu-lkmpd8-WhARmk3eF5Jt91aE3o'
BOT_USERNAME: Final = '@simple_scratch_bot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your scratch bot!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a scratch bot! Please type something so I can respond!")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")


# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there, How can I help you!'
    if 'how are you' in processed:
        return 'I am good!'
    if 'i love this bot' in processed:
        return 'Thank you!'
    if 'who created you' in processed:
        return 'I was created by Umaiorubagan!'
    if 'tell some random jokes' in processed:
        return 'One joke, coming up! What is a sea monster’s favorite snack? Ships and dip.'
    if 'give some interview tips!' in processed:
        return (
            "Certainly! Here are some tips to help you prepare for an interview:\n\n"
            "- Research the Company: Understand the company's mission, values, products/services, and recent news. This knowledge will demonstrate your interest and suitability for the role.\n\n"
            "- Know the Job Description: Familiarize yourself with the job requirements and responsibilities. Be ready to discuss how your skills and experiences align with what the company is seeking.\n\n"
            "- Practice Common Interview Questions: Prepare responses to common interview questions such as 'Tell me about yourself', 'What are your strengths and weaknesses?', and 'Why do you want to work here?' Practice articulating your answers clearly and concisely.\n\n"
            "- Highlight Your Achievements: Prepare specific examples of your accomplishments that demonstrate your skills and qualifications for the position. Use the STAR method (Situation, Task, Action, Result) to structure your answers.\n\n"
            "- Dress Appropriately: Choose professional attire that aligns with the company culture. If you're unsure, it's better to overdress than underdress.\n\n"
            "- Arrive Early: Plan to arrive at least 10-15 minutes early for the interview. This will give you time to compose yourself and fill out any necessary paperwork.\n\n"
            "- Bring Copies of Your Resume: Even if you've already submitted your resume online, bring several printed copies to the interview. This shows preparedness and allows you to reference specific details during the conversation.\n\n"
            "- Ask Questions: Prepare insightful questions to ask the interviewer about the company, team dynamics, or the role itself. This demonstrates your interest and engagement.\n\n"
            "- Body Language: Maintain good posture, make eye contact, and offer a firm handshake. Non-verbal communication is important and can leave a lasting impression.\n\n"
            "- Follow-Up: Send a thank-you email or note to the interviewer within 24 hours of the interview. Express your gratitude for the opportunity and reiterate your interest in the position.\n\n"
            "Remember, interviewing is as much about assessing whether the company is a good fit for you as it is about showcasing your qualifications. Be yourself, stay confident, and show enthusiasm for the opportunity. Good luck!"
        )
    if 'which is best chatgpt (or) scratch bot' in processed:
        return 'Scratch BOT!'
    return "I do not understand what you wrote..."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)

