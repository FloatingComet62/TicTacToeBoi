import discord
import random
from discord.ext import commands
import os

class Game:
    def __init__(self, p1:int, p2:int):
        self.p1 = p1
        self.p2 = p2
        self.grid = [[0]*3, [0]*3, [0]*3]
        self.turn = random.choice([p1, p2])
        self.p2_ok = False

class TicTacToe(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client
        self.games = []
    
    @commands.command()
    async def match(self, ctx: commands.context.Context, opponent: discord.Member):
        if ctx.author.id in [x.p1 for x in self.games] and ctx.author.id in [x.p2 for x in self.games if x.p2_ok]:
            ctx.send("You are already in a game!")
        else:
            self.games.append(Game(ctx.author.id, opponent.id))
            await ctx.send(f"{opponent.mention} Type `y` in the chat to accept the match (This will expire in 60 seconds)")
            def check(m):
                return m.author.id == opponent.id and m.content=='y'
            msg = await self.client.wait_for('message', check=check, timeout=60)
            for g in self.games:
                if g.p2 == msg.author.id:
                    g.p2_ok = True
                    break
            await ctx.send(f"Match started lol {g.__dict__}")

def setup(bot):
    bot.add_cog(TicTacToe(bot))