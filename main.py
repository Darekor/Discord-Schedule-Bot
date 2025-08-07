import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go, {bot.user.name}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

@bot.command()
async def dm(ctx):
    await ctx.author.send(f"You suck!")

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)