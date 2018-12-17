import discord

from discord.ext import commands

from discord.ext.commands import Bot

import youtube_dl

import random

from os import environ

import asyncio

import time

import random

import datetime

import math

import requests


import random


import datetime

import math

import sys

import base64

import hashlib

import traceback

import string

import inspect

import json

import aiohttp

import websockets

import urllib.request

import logging

from collections import Counter

import os

import colorsys

import socket
from os import environ
from lxml import html
import asyncio
import time
import random
import datetime
import math
import requests
import sys
import base64
import hashlib
import traceback
import string
import inspect
import json
from cleverwrap import CleverWrap
import config
import utils
import aiohttp
import websockets
from bs4 import BeautifulSoup
import urllib.request
import logging
import colorsys
import socket

bot = Bot(description="like is best", command_prefix=">")


print(f"Connecting your bot to discord!")
# remove help
bot.remove_command('help')
# variables

botavatar = "https://cdn.discordapp.com/avatars/507241518524923904/dea61e2eb1de8f94e8460d707bfe0d08.webp?size=1024"

@bot.event
async def on_ready():
    print("STFU LETS GO!")
# help


@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      embed = discord.Embed(color=0xC72323)
      embed.set_author(name='Help')
      embed.add_field(name = 'If you react with ⚙ ',value ='**This will show all the __Moderation commands__ which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.**',inline = False)
      embed.add_field(name = 'If you react with 👥 ',value ='**This will show the all the __General commands__ which are usable by everyone.**',inline = False)
      embed.add_field(name = 'If you If you react with 😁 ',value ='**You will get the commands and information about __fun commands.__**',inline = False)
      embed.add_field(name="Bot Invite", value="[👉 Invite Like HERE 👈]( https://discordapp.com/api/oauth2/authorize?client_id=507241518524923904&,permissions=8&scope=bot)")
      embed.add_field(name="Donation Link", value="[HERE](https://paypal.me/CocoGT)")
      embed.add_field(name="Wanna vote for Like?", value="[👉 UPVOTE ME PLEASE 👈](https://discordbots.org/bot/507241518524923904/vote)")
      embed.set_thumbnail(botavatar)
      dm_message = await client.send_message(author,embed=embed)
      react_1 = '⚙'
      react_2 = '👥'
      react_3 = '😁'
      await client.add_reaction(dm_message, react_1)
      await client.add_reaction(dm_message, react_2)
      await client.add_reaction(dm_message, react_3)


# help moderation

@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '⚙':

        embed = discord.Embed(color=0xC72323)
 
      embed.add_field(name='⚙__Moderation Commands__⚙', value = '**THIS COMMANDS NEEDS PERMISION FROM OWNER TO USE THEM**\n``>help for more information.``')
        embed.add_field(name='>kick', value = ' kick a user from the server/guild.')
        embed.add_field(name='>ban', value = ' ban a user from the server/guild.')
        embed.add_field(name='>slowclear', value = ' it will slowy clearing all messages from the channel.')
        embed.add_field(name='>warn', value = ' warn a user from the server/guild.')
        embed.add_field(name='>decide', value = ' this will decide you from what the bot wants.')
        embed.add_field(name='>secretkick', value = ' this will ban a user without showing to logs.')
        embed.add_field(name='>secretkick', value = '  this will kick a user without showing it to logs.')
        embed.add_field(name='>clear', value = ' this will clear on how many do you like to clear.')
        embed.add_field(name='>slowmode', value = ' this will turn on the slow mode.')
        embed.add_field(name='>config_slowmode', value = ' config the slowmode.')
        embed.add_field(name='>renamerole', value = '  it will Rename a role.')
        embed.add_field(name='>renameserver', value = ' it will rename the server/guild name.')
        embed.add_field(name='>nick', value = ' this will nick the user.')
        embed.add_field(name='>textchannel', value = ' this will create a text channel.')
        embed.add_field(name='>voicechannel', value = ' this will create a voice channel.')
        embed.add_field(name='>nickall', value = ' this will nickname all users he can.')
        embed.add_field(name='>renamechannel', value = 'this will rename a text/voice channel.')
      embed.add_field(name='>emojirename', value = ' this will rename an emoji.')
        embed.add_field(name='>announce', value = '  this will dm all users to announce.')
        react_1 = '👥'
        react_2 = '😁'
        await bot.add_reaction(react_message, reaction)


      if reaction.emoji == '👥':
        embed = discord.Embed(color=0xC72323)

        embed.add_field(name = '👥__General commands__👥', value= '``>help for more information.``')
        embed.add_field(name='>userinfo', value = 'to  see the users information.')
        embed.add_field(name='>botinfo', value = " this will show Like's information.")
        embed.add_field(name='>serverinfo', value = ' this will show the information of server/guild.')
        embed.add_field(name='>invite', value = ' to invite me in your server/guild.')
        embed.add_field(name='>serverinfo', value = ' to show all users on the server/guild.')
        embed.add_field(name='>servercount', value = ' it will show on how many server/guild is Like in.')
        embed.add_field(name='>stringgen', value = ' this will string gen the numbers.')
        embed.add_field(name='>avatar', value = ' this will show the avatar of the user.')
        embed.add_field(name='>say', value = ' this will say you want me to say.')
        embed.add_field(name='>embed', value = ' this will embed the message you said.')
        embed.add_field(name='>qr', value = ' this will make the message to like in QR.')
        embed.add_field(name='>google', value = ' this will search froom google and send you the link.')
        embed.add_field(name='>youtube', value = '  this will search from youtube and send you th link.')
        embed.add_field(name='>encode', value = ' this will encode you want.')
        embed.add_field(name='>randomint', value = ' this will randomly pick letters 1 up to 100.')
        embed.add_field(name='>ping', value = ' this will show the ping/ms.')
        embed.add_field(name='>customint', value = ' the bot will randomly pick letters you want.')
        embed.add_field(name='>embedcode', value = ' this will show you the embed code.')
        embed.add_field(name='>codeinfo', value = ' this will show you the codes information.')
        embed.add_field(name='>poll', value = ' it will gonna make  poll.')
        embed.add_field(name='>botsearch', value = ' this will search a bot for you.')
        embed.add_field(name='>topbots', value = ' this is the list of top bots.')
        embed.add_field(name='>serverowner', value = ' this will show the information of the server/guild owner.')
        embed.add_field(name='>statcheck', value = ' this will show you the status of a user.')
        embed.add_field(name='>gamecheck', value = ' this will show you on what the user doing.')
        embed.add_field(name='>vote', value = ' it shows the voting link for Like.')
        embed.add_field(name='>channelinfo', value = ' this will show you the information of the channel.')
        embed.add_field(name='>docs', value = ' this will send you the link for discord docs.')
        embed.add_field(name='>nick', value = ' this will nickname a user.')
        embed.add_field(name='>emojis', value = ' this will show you all of the emojis on the server/guild.')
        embed.add_field(name='>membernames', value = ' this will dm all users name on the server/guild.')
        embed.add_field(name='>kickme', value = ' you will ask for kick your self.')
        embed.add_field(name='>userip', value = ' this will show the users ip, this will work if the user is in the database.')
        react_1 = '⚙'
        react_2 = '😁'
        await bot.add_reaction(react_message, reaction)


      if reaction.emoji == '😁':
        embed = discord.Embed(color=0xC72323)

        embed.add_field(name='😁__Fun Coammands__😁', value='``>help for more information.``')
        embed.add_field(name='>8ball', value = ' this will answer your question.')
        embed.add_field(name='>hug', value = '  you will hug the user.')
        embed.add_field(name='>gender', value = '  this will say the users gender.')
        embed.add_field(name='>fbi', value = ' fbi fbi fbi!!!!')
        embed.add_field(name='>joke', value = ' this will show you a random joke from the database.')
        embed.add_field(name='>dadjoke', value = ' this will show you a random dadjoke from the database.')
        embed.add_field(name='>skincolor', value = ' this will say the users skin color.')
        embed.add_field(name='>sapnupuas', value = ' this will show you the conversation in the Mccdonalds secret area.')
        embed.add_field(name='>howgay', value = ' this will show the gay percentage from the user.')
        embed.add_field(name='>hack', value = ' this will hack the user.')
        embed.add_field(name='>bomb', value = ' you will plant a bomb to the user.')
        embed.add_field(name='>slap', value = ' you will slap the user.')
        embed.add_field(name='>whois', value = ' this will show who is the user.')
        embed.add_field(name='>rolldice', value = ' this will roll the dice and pick number 1 to 6.')
        embed.add_field(name='>hairdye', value = ' this will hairdye the user.')
        embed.add_field(name='>height', value = ' this will say the height of the user.')
        embed.add_field(name='>talentcheck', value = ' this will show you the talent of the user.')
        embed.add_field(name='>howto', value = ' you will ask how to do something.')
        embed.add_field(name='>shoot', value = ' you will shoot the user.')
        embed.add_field(name='>lenny', value = ' this will show the lennys face!!.')
        embed.add_field(name='>autistcheck', value = ' this will say the users austistic percentage.')
        embed.add_field(name='>tweet', value = ' this will tweet the username and text.')
        embed.add_field(name='>awooify', value = ' this will awooify the user.')
        embed.add_field(name='>ship', value = ' this will show how the users love each other lol.')
        react_message = await bot.send_message(user,embed=embed)
        react_1 = '⚙'
        react_2 = '👥'
        await bot.add_reaction(react_message, reaction)

bot.run(os.environ['mytoken'])