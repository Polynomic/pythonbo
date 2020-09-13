import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os
client = commands.Bot(command_prefix = 's!')

@client.event
async def on_ready():
    print('Bot is online!')

@client.event
async def on_member_join(member):
    print(f'{Member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

client.run('NzU0NDEwMTIyODU1NDQ4NzI5.X10VLQ.hgEK2yvGrXkUktqBIgqZWEh3UNk')
