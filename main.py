#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

from os import environ

from pyrogram import Client
plugins = dict(
        root="plugins"
    )
bot = Client(
    "QR CODE BOT",
    bot_token = environ.get('BOT_TOKEN'),
    api_id = environ.get('API_ID') , 
    api_hash = environ.get('API_HASH'),
    plugins = plugins
)
bot.run()
