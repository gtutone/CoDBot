#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:17:54 2021
@author: gabrieltutone
"""

# client = commands.Bot(command_prefix='!')
#
# @client.event
# async def on_ready():
#     print('Bot is ready')
#
# @client.event
# async def on_member_join(member):
#
# client.run('Nzk2NjE5NjIxNTM1OTczMzc2.X_aj1g.vOKGxNl5sM8eUniJf-cPczhduS8')

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
PlayedGame = 'Card of Darkness'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(PlayedGame))

@client.command()
async def

client.run('Nzk2NjE5NjIxNTM1OTczMzc2.X_aj1g.vOKGxNl5sM8eUniJf-cPczhduS8')