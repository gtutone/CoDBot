#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:17:54 2021
@author: gabrieltutone
"""

import discord
import re
import csv
from fuzzywuzzy import process

def CardSearch(card):
    CardDesc = ''
    CardTitles = []
    # Read the csv file containing the cards
    with open('CardsList.csv', newline='') as csvfile:
        CardReader = csv.DictReader(csvfile, delimiter=',')

        # Find card with highest fuzzy match
        for row in CardReader:
            CardTitles.append(row['Title'])
        FuzzyMatch = process.extractOne(card, CardTitles)
        FuzzyRatio = FuzzyMatch[1]
        CardMatch = str(FuzzyMatch)[2:-6]
        if FuzzyRatio != 100:
            print('Did you mean: ' + CardMatch + '?')

        else:
            # Iterate over all the cards and check if the title matches
            for row in CardReader:
                if CardMatch == row['Title']:
                    # If card has no tier modifiers
                    if (row['Level 1'] or row['Level 1'] or row['Level 1']) == 'n/a':
                        CardDesc = str(row['Title']) +'\n'+ str(row['Description']) +'\n'+ 'No tier modifiers'
                        return CardDesc

                    # If card has tier modifiers, append them to output
                    else:
                        CardDesc = str(row['Title']) +'\n'+ str(row['Description']) +'\n'+\
                                   'Tier 1: ' + str(row['Level 1']) + ', '+\
                                   'Tier 2: ' + str(row['Level 2']) + ', '+\
                                   'Tier 3: ' + str(row['Level 3'])
                        return CardDesc

    # If no card found, let user know
    if CardDesc == '':
        CardDesc = 'No card found'
        return CardDesc

client = discord.Client()

# Print confirmation that bot is logged in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Currently unused. If uncommented, also uncomment 'import commands'
# client = commands.Bot(command_prefix='!')

# Add the "Playing: CoD" rich presence text to the bot
PlayedGame = 'Card of Darkness'
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

    # Make message lowercase, so it's easier to search for keywords
    messageLow = message.content.lower()

    # Look for messages that contain 'card'
    if 'card' in messageLow:
        # Find the card in the message and make every first letter uppercase
        CardExtract = str(re.findall('card of \w+', message.content, re.IGNORECASE)).title()[2:-2]
        # Lookup card using the CardSearch function
        CardLookup = CardSearch(CardExtract)
        # Send card description text to channel
        await message.channel.send(CardLookup)

    else:
        await message.channel.send('No card contained in message')

# Discord bot token is stored in a separate file, ignored by gitHub for privacy
with open("token.txt", "r", encoding="utf-8") as token:
    botToken = token.read()

client.run(botToken)