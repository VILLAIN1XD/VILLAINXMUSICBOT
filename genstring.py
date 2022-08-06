#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @ll_villain_ll
# Rocks © @ll_villain_ll
# Owner VILLAIN 
# DEV RAJ 
# All rights reserved. ©vILLAIN


import asyncio

from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print(
        "\nHERE IS YOUR PYROGRAM STRING SESSION, COPY IT, DON'T SHARE IT WITH YOUR GF !\n"
    )
    print(f"\n{ss}\n")


asyncio.run(main())
