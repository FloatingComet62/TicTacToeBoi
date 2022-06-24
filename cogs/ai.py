import discord
from discord.ext import commands
import os

class AI(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def tic(self, ctx):
        respond = discord.Embed(title="Tic Tac Toe", description=(("⬛"*3)+"\n")*3)
        await ctx.send(embed=respond)

def setup(bot):
    bot.add_cog(AI(bot))