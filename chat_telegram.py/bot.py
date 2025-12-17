import os
from langchain_groq import ChatGroq
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

chat = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def conversar(pergunta: str) -> str:
    resposta = chat.invoke([
        ("system", "você é um assistente."),
        ("human", pergunta)
    ])
    return resposta.content

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("bot online 🚀")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resposta = conversar(update.message.text)
    await update.message.reply_text(resposta)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()

if __name__ == "__main__":
    main()