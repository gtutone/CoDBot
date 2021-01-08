#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:17:54 2021
@author: gabrieltutone
"""

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
PlayedGame = 'Card of Darkness'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(PlayedGame))

# @client.command()
# async def

with open("token.txt", "r", encoding="utf-8") as token:
    botToken = token.read()

client.run(botToken)