import discord

from discord.ext import commands

from discord.ext.commands import Bot

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

import config
import utils
import aiohttp
import websockets
from bs4 import BeautifulSoup
import urllib.request
import logging
import colorsys
import socket
import asyncio
import os
import json
import random
import time

print("Lets go+++++++++++++++++++++++ boiiiiiiiiiiuuuuuuuu")

bot = Bot(description="Like is best", command_prefix=">")                     
bot.remove_command('help')

@bot.event
async def on_member_join(member):
    with open("users.json", "r") as f: 
        users = json.load(f)

        await update_data(users, member) 

            with open("users.json", "w") as f:
            json.dump(users, f) 


@bot.event
async def on_message(message):
    with open("users.json", "r") as f:
        users = json.load(f)

        if message.author.bot:
            return
        if message.channel.is_private:
            return
        else:
            await update_data(users, message.author, message.server)
            number = random.randint(5,10)
            await add_experience(users, message.author, number, message.server)
            await level_up(users, message.author, message.channel, message.server)

        with open("users.json", "w") as f:
            json.dump(users, f)
    await bot.process_commands(message)

async def update_data(users, user, server):
    if not user.id + "-" + server.id in users:
        users[user.id + "-" + server.id] = {}
        users[user.id + "-" + server.id]["experience"] = 0
        users[user.id + "-" + server.id]["level"] = 1
        users[user.id + "-" + server.id]["last_message"] = 0

async def add_experience(users, user, exp, server):
    if time.time() - users[user.id + "-" + server.id]["last_message"] > 10: 
        users[user.id + "-" + server.id]["experience"] += exp
        users[user.id + "-" + server.id]["last_message"] = time.time()
    else:
        return

async def level_up(users, user, channel, server):
    experience = users[user.id + "-" + server.id]["experience"]
    lvl_start = users[user.id + "-" + 
server.id]["level"]
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await bot.send_message(channel, f":tada: Congrats {user.mention}, you levelled up to level {lvl_end}!")
        users[user.id + "-" + server.id]["level"] = lvl_end

#XP/Level
@bot.command(pass_context=True)
async def xp(ctx, user: discord.Member = None):
    """says your/mentions XP count """
    user = user or ctx.message.author
    with open('users.json') as f:
        data = json.load(f)

    if data.get(user.id) is not None:
        await bot.say(f'XP count is at {data[user.id]["experience"]}.')
    else:
        await bot.say(f'I cannot see {user.mention} in my list of users.')

#--------------------------------------

@bot.command(pass_context=True)
async def level(ctx, user: discord.Member = None):
    """says your/mentions level """
    user = user or ctx.message.author
    with open('users.json') as f:
        data = json.load(f)

    if data.get(user.id) is not None:
        await bot.say(f'User level is {data[user.id]["level"]}.')
    else:
        await bot.say(f'I cannot see {user.mention} in my list of users.')

bot.run(os.environ['BOT_TOKEN'])