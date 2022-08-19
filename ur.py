import discord
from discord.ext import commands, tasks
import os
import asyncio

prefix='!'
n=0

intents=discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)

client = commands.Bot(command_prefix=prefix, intents=intents)
@client.event
async def on_ready():
    print('Bot is online')
    await client.change_presence(activity=discord.Game('Security'))
     ctx.guild.text_channels:
             await c.send('@everyone ') # Put the messages you want to be spammed here
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             client.run('MTAwOTk4MjY1Mzg5NTgwNzExNg.GLW5tk.zw7EM2i9MWcBS98nFzYXUcYR2KDGiKi3BDErUA')