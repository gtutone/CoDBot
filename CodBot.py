#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:17:54 2021
@author: gabrieltutone
"""

import discord
# from discord.ext import commands
from Cards import CardDict
import re
import os

# Currently unused. If uncommented, also uncomment 'import commands'
# client = commands.Bot(command_prefix='!')
PlayedGame = 'Card of Darkness'

# Add the "Playing: CoD" rich presence text to the bot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(PlayedGame))

# Bot listens for any message coming in
@client.event
async def on_message(message):
    # Ignore any message that comes from the bot itself
    if message.author == client.user:
        return

    # Look for messages that contain 'card of'
    if 'Card of' or 'card of' in message.content:
        # Find the card in the message and make every first letter uppercase
        CardExtract = str(re.findall('card of \w+', message.content, re.IGNORECASE)).title()[2:-2]
        # Lookup card description in the Cards dictionary
        CardLookup = CardDict[CardExtract]
        # Add the card name to the description to be more user friendly
        Description = str(CardExtract + ': ' + CardLookup)
        await message.channel.send(Description)

Discord bot token is stored in a separate file, ignored by gitHub for privacy
with open("token.txt", "r", encoding="utf-8") as token:
    botToken = token.read()

# client.run(os.getenv('TOKEN'))