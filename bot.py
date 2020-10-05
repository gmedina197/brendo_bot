import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = commands.Bot(command_prefix="!v")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="brendo")
async def brendo(ctx):
    await ctx.send("brenom")

@bot.event
async def on_message(message):
    await message.add_reaction('<:xuxubre:757681263808217138>')
    
    await message.add_reaction('🇧')
    await message.add_reaction('🇷')
    await message.add_reaction('🇪')
    await message.add_reaction('🇳')
    await message.add_reaction('🇴')
    await message.add_reaction('🇲')

    await message.add_reaction('<:kikobre:757680956017475664>')

bot.run(BOT_TOKEN)