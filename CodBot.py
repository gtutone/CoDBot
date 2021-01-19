#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:17:54 2021
@author: gabrieltutone
"""

import discord
import csv
from fuzzywuzzy import process
from discord.ext import commands

def CardSearch(card):
    CardDesc = ''
    CardTitles = []

    # Read the csv file containing the cards and find highest fuzzy match
    with open('CardsList.csv', newline='') as csvfile:
        CardReader = csv.DictReader(csvfile, delimiter=',')

        # Find card with highest fuzzy match
        for row in CardReader:
            CardTitles.append(row['Title'])
        FuzzyMatch = process.extractOne(card, CardTitles)
        CardMatch = str(FuzzyMatch)[2:-6]
        # Sometimes slice one additional char at end, or else it leaves a trailing apostrophe in string
        if CardMatch.endswith("\'") is True:
            CardMatch = CardMatch[:-1]

    # Re-iterate through the csv, and match the fuzzy match card with its description
    with open('CardsList.csv', newline='') as csvfile2:
        CardReader2 = csv.DictReader(csvfile2, delimiter=',')

        # Iterate over all the cards and check if the title matches
        for row2 in CardReader2:
            if CardMatch == row2['Title']:
                print(str(row2['Type']))

                # If card is Card of Darkness, check the level modifiers
                if str(row2['Type']) == 'Card of Darkness':

                    # If card is CoD and has no level modifiers
                    if (row2['Level 1'] or row2['Level 1'] or row2['Level 1']) == 'n/a':
                        CardDesc = str(row2['Title']) + '\n'+ str(row2['Description']) +'\n'+\
                        'No level modifiers'+'\n'+'Zone: '+str(row2['Zone']) + '\n'+'Type: '+str(row2['Type'])
                        return CardDesc

                    # If card has level modifiers, append them to output
                    else:
                        CardDesc = str(row2['Title']) +'\n'+ str(row2['Description']) +'\n'+ \
                                   'Level 1: X=' + str(row2['Level 1']) + ', '+\
                                   'Level 2: X=' + str(row2['Level 2']) + ', '+\
                                   'Level 3: X=' + str(row2['Level 3']) + '\n'+\
                                   'Zone: ' + str(row2['Zone']) + '\n' +\
                                   'Type: ' + str(row2['Type'])
                        return CardDesc

                # If card is a monster, shows zone where it's from
                elif str(row2['Type']) == 'Monster':
                    CardDesc = str(row2['Title']) +'\n'+str(row2['Description']) +'\n'+\
                               'Zone: ' + str(row2['Zone']) + '\n'+'Type: '+str(row2['Type'])
                    return CardDesc

                # If card is not Card of Darkness, don't display modifiers
                else:
                    CardDesc = str(row2['Title']) +'\n'+str(row2['Description']) +'\n'+'Type: '+str(row2['Type'])
                    return CardDesc

        # If somehow no card found, let user know
        if CardDesc == '':
            CardDesc = 'No card found'
            return CardDesc

bot = commands.Bot(command_prefix='!')

# Print confirmation that bot is logged in
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

# Add the "Playing: CoD" rich presence text to the bot
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game('Card of Darkness'))

# Command to let users lookup card descriptions
@bot.command(name='cod', help='Lookup card descriptions')
async def CardLookup(ctx, *card):
    CardQuery = ' '.join(card)
    CardDescription = CardSearch(CardQuery)
    await ctx.send(CardDescription)

# Discord bot token is stored in a separate file, ignored by gitHub for privacy
with open("token.txt", "r", encoding="utf-8") as token:
    botToken = token.read()

# client.run(botToken)
bot.run(botToken)