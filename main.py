# main.py
import discord
from discord.ext import commands
from telegram import Bot
import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

telegram_bot = Bot(token=TELEGRAM_BOT_TOKEN)

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', self_bot=True, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.channel.id != DISCORD_CHANNEL_ID:
        return
    if message.author == bot.user:
        return

    try:
        await telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message.content)
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

bot.run(DISCORD_TOKEN)
