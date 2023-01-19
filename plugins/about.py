import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Origional BOT :- <a href='https://t.me/Rename_pro_v1_bot'>Pro Rename</a>\nCreater :- <a href='https://t.me/Farooq_is_KING'>🦋Farooq🦋</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- Heroku\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you **<a href='https://t.me/Farooq_is_KING'>Farooq</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/Farooq_is_KING'>**Farooq**</a> ❤️",quote=True)
