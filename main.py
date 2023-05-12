from dotenv import load_dotenv
import discord
import os

load_dotenv()

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

bot = discord.Client(intents=discord.Intents.default())

bot.run(DISCORD_TOKEN)