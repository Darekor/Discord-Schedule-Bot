import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import datetime


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

CALENDAR = ["ПН","ВТ","СР","ЧТ","ПТ","СБ","ВС"]


@bot.event
async def on_ready():
    print(f"We are ready to go, {bot.user.name}")

@bot.hybrid_command()
async def schedule(ctx, *, quest="", window = 7):
    ping = ""
    if quest=="":
        text = "Когда собираемся?"
    else:
        text = f"Когда собираемся на {quest}?"
        role = next(filter(lambda x: x.name==quest,ctx.guild.roles),None)
        if (role!=None):
            ping = role.mention
            await ctx.send(content = ping)
    newpoll = discord.Poll(text, datetime.timedelta(hours=1), multiple=True)
    for i in range(window):
        newpoll = newpoll.add_answer(text=CALENDAR[(datetime.date.today()+datetime.timedelta(days=i)).weekday()],emoji=None)
    await ctx.send(poll = newpoll)


@bot.command()
async def dm(ctx):
    await ctx.author.send(f"You suck!")

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)