from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

if os.path.isfile(".env"):
    load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=intents)
bot.load_extension('jishaku')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong :ping_pong: (Latency {round(bot.latency)})')

bot.run(os.getenv("TOKEN"))