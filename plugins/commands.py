import os
import logging
import time
import string
import traceback
from pyrogram import Client, filters
import datetime
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from Config import Config

logging.basicConfig()
logger = logging.getLogger(__name__)


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=f"Hello {message.from_user.mention},\nI'm a telegram Education Bot From BRYLL EDUCATION bot by @bryllbots",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(START_BTN)
    )

START_BTN = [[
     InlineKeyboardButton('Subjects', callback_data='subject_cd')
     ],[
     InlineKeyboardButton('❌ Close ✖', callback_data='close')
     ]]

@app.on_message(filters.command("subject"))
async def subject(client,message):
    if message.from_user.id not in AUTH_USERS:
        await message.reply_text(
            text=f"**Hey {message.from_user.mention}!\n\n👉 You have not purchased our premium plan. To use this command kindly purchase our premium plan.\n\n👉 Details of the premium plan👇👇👇\n\nIf you are interested in our service then you can buy the plan by contacting our helpdesk👇👇👇**",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton('Contact Our Helpdesk', url=f'https://telegram.me/bryll_helpdesk_bot')
                ]]
              )
            )
        return
    await message.reply_text(
        text=f"Hey! Choose the Subject",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(SUBJECT_BTN)
        )

SUBJECT_BTN = [[
    InlineKeyboardButton('Biology', callback_data='biology_cd')
    ],[
    InlineKeyboardButton('Physics', callback_data='physics_cd')
    ],[
    InlineKeyboardButton('Chemistry', callback_data='chemistry_cd')
    ]]
                        

@app.on_message(filters.command("biology"))
async def biology(client,message):
    await message.reply_text(
        text=f"Hey! {message.from_user.mention} Choose the Chapter which you want to study",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(BCHAPTER_BTN)
    )

BCHAPTER_BTN = [[
     InlineKeyboardButton('Chapter 01', url=f'https://d2bps9p1kiy4ka.cloudfront.net/5eb393ee95fab7468a79d189/50c941fa-52bc-4714-9cc3-e1af8b86b590.pdf')


     ],[
     InlineKeyboardButton('Chapter 02', callback_data='bch1_cd')
     ],[
     InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')
     ],[
     InlineKeyboardButton('⏪ Back ⏪', callback_data='subject_cd')
     ]]


@app.on_message(filters.command("physics"))
async def physics(client,message):
    await message.reply_text(
        text=f"Hey! {message.from_user.mention} Choose the Chapter which you want to study",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(PCHAPTER_BTN)
     )
    
PCHAPTER_BTN = [[
      InlineKeyboardButton('Chapter 01', url=f'https://telegram.me/bryllbots')
      ],[
      InlineKeyboardButton('Chapter 02', url=f'https://telegram.me/bryllbots')
      ],[
      InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')
      ],[
      InlineKeyboardButton('⏪ Back ⏪', callback_data='subject_cd')
      ]]


@app.on_message(filters.command("chemistry"))
async def chemistry(client,message):
    await message.reply_text(
        text=f"Hey! {message.from_user.mention} Choose the Chapter which you want to study",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(CCHAPTER_BTN)
    )
    
CCHAPTER_BTN = [[
       InlineKeyboardButton('Chapter 01', url=f'https://telegram.me/bryllbots')
       ],[
       InlineKeyboardButton('Chapter 02', url=f'https://telegram.me/beyllbots')
       ],[
       InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')
       ],[
       InlineKeyboardButton('⏪ Back ⏪', callback_data='subject_cd')
       ]]
    

@app.on_message(filters.command("me"))
async def me(client,message):
    await message.reply_text(
        text=f"""**Your Details**
        
**First Name:-** <code>{message.from_user.first_name}</code>
**Last Name:-** <code>{message.from_user.last_name}</code>
**User Name:-** @{message.from_user.username}
**User ID:-** <code>{message.from_user.id}</code>""",
        disable_web_page_preview=True,
      )
