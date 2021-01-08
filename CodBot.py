#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:17:54 2021
@author: gabrieltutone
"""

import discord
from discord.ext import commands
from Cards import CardDict
import re

client = commands.Bot(command_prefix='!')
PlayedGame = 'Card of Darkness'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(PlayedGame))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'Card of' or 'card of' in message.content:
        # Find the card in the message and make every first letter uppercase
        CardExtract = str(re.findall('card of \w+', message.content, re.IGNORECASE)).title()[2:-2]
        CardLookup = CardDict[CardExtract]
        Description = str(CardExtract + ': ' + CardLookup)
        await message.channel.send(Description)

with open("token.txt", "r", encoding="utf-8") as token:
    botToken = token.read()

client.run(botToken)