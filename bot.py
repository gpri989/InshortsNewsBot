import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from main import neget
from config import API_ID, API_HASH, BOT_TOKEN
import random
import time

app = Client(
    "my_bot",
    api_id=API_ID, api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
@app.on_message(filters.command("start"))
async def start_command(_, message):
    await message.reply_text(f"**Hey {message.from_user.first_name}! Welcome to News Bot š¤ \nTry /help to Get Started**")

@app.on_message(filters.command("help"))
async def help_command(_, message):
    await message.reply_text("**Just Select News Category Name from Menu\nš¢ For Menu /categories**")

@app.on_message(filters.command("categories"))
async def categories_command(_, message):
    CAT_BUTTONS = [
        [ 
            ("All News"),
            ("Trending"),
            ("Top Stories")
        ],
        [
            ("National"),
            ("Business"),
            ("Politics")
        ],
        [
            ("Sports"),
            ("Technology"),
            ("World")
        ],
        [
            ("Entertainment"),
            ("Hatke"),
            ("Education")
        ],
        [
            ("Startups"),
            ("Automobile"),
            ("Science")
        ],
        [
            ("Travel"),
            ("Miscellaneous"),
            ("Fashion")
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(CAT_BUTTONS, one_time_keyboard=False, resize_keyboard = True)
    await message.reply(text = "**Choose From News Category Menu Below šš»**", reply_markup=reply_markup)

@app.on_message(filters.text)
async def search(_, message):
    rn = message.text.lower()
    rn = rn.replace(" ", "_")
    try:
        fet = neget(rn)['articles']
        javl = neget(rn)['total']
        j = random.randint(0, javl)
        furl = f"{fet[j]['source_url']}"
        stime = fet[j]['created_at']/1000
        my_time = time.strftime('%-d %B, %A, %I:%M %p', time.localtime(stime))
        furl = furl.replace(" ", "")
        str = f"**š° {fet[j]['title']}**\n\n{fet[j]['description']}\n\nšļø ```{my_time}```\nš¹ **From :** __{fet[j]['source_name']}__"
        img = fet[j]['image_url']
        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Read Full Story š",
                            url=furl
                        )
                    ]
                ]
            )
        await message.reply_photo(photo = img, caption = str, reply_markup=keyboard)
    except IndexError:
        await message.reply_text("**News Category Not Found ā**")
print("Bot Alive")
app.run()