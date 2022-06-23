import discord
from discord.ext import commands
import os

class AI(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(bot):
    bot.add_cog(AI(bot))