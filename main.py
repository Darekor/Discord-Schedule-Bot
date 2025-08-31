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

bot = commands.Bot(command_prefix='/', intents=intents)

CALENDAR = ["ПН","ВТ","СР","ЧТ","ПТ","СБ","ВС"]
LENGTH = [1,2,3,4,5,6,7,8,9,10]



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.tree.sync()

@bot.hybrid_command(description="Make a poll for specific roll schedule")
async def schedule(ctx:commands.Context, role:discord.Role=None, duration:int=7):
    if role==None or role==discord.Role.is_default: 
        text = "Когда собираемся?"
    else:
        text = f"Когда собираемся на {role.name}?"
        await ctx.send(content = role.mention)
    newpoll = discord.Poll(text, datetime.timedelta(days=7), multiple=True)
    if duration not in range(1,10):
        duration=7
    for i in range(duration):
        newpoll = newpoll.add_answer(text=CALENDAR[(datetime.date.today()+datetime.timedelta(days=i+1)).weekday()],emoji=None)
    await ctx.send(poll = newpoll)



@bot.command()
async def dm(ctx):
    await ctx.author.send(f"You suck!")


bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)