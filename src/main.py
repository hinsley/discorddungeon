#!/usr/bin/env python

import discord
import json
from discord.ext.commands import Bot


client = Bot(description="AIDungeon interface bot",
             command_prefix="]")

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def do(ctx, *args):
    await ctx.send(f"```> You {' '.join(args)}```")

@client.command()
async def say(ctx, *args):
    await ctx.send(f"```You say, \"{' '.join(args)}\"```")

@client.command()
async def story(ctx, *args):
    await ctx.send(f"```{' '.join(args)}```")


with open("config.json") as f:
    cfg = json.load(f)
    client.run(cfg["API Token"])
