from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

if os.path.isfile(".env"):
    load_dotenv()

cogs = ['cogs.ai']
intents = discord.Intents.default()
client = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=intents)
client.load_extension('jishaku')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

for cog in cogs:
    client.load_extension(cog)

@client.event
async def on_connect():
    activity = discord.Activity(name="Tic Tac Toe", type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong :ping_pong: (Latency {round(client.latency)})')

client.run(os.getenv("TOKEN"))