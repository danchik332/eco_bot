import discord
from discord.ext import commands
import os, random, requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

list = ['Сокращайте использование пластика',' Экономьте электроэнергию','Помогайте сохранять воду','Сортируйте отходы'
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def eco(ctx):
    element = random.choice(list)
    await ctx.send(element)
 
 
bot.run("token")


