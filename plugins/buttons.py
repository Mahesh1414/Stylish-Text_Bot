from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
class BTNS(object):
  
  START_BTN = [[
     InlineKeyboardButton('Subjects', callback_data='subject_cd')
     ],[
     InlineKeyboardButton('❌ Close ✖', callback_data='close')
     ]]
  
  SUBJECT_BTN = [[
    InlineKeyboardButton('Biology', callback_data='biology_cd')
    ],[
    InlineKeyboardButton('Physics', callback_data='physics_cd')
    ],[
    InlineKeyboardButton('Chemistry', callback_data='chemistry_cd')
    ]]
  
  BCHAPTER_BTN = [[
     InlineKeyboardButton('Chapter 01', url=f'https://d2bps9p1kiy4ka.cloudfront.net/5eb393ee95fab7468a79d189/50c941fa-52bc-4714-9cc3-e1af8b86b590.pdf')
     ],[
     InlineKeyboardButton('Chapter 02', callback_data='bch1_cd')
     ],[
     InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')
     ],[
     InlineKeyboardButton('⏪ Back ⏪', callback_data='subject_cd')
     ]]
