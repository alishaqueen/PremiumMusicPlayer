from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
ð â°Ç«á´á´á´É´âá´ÊÉªsÊá´â± á´É´ á´á´á´ á´É´á´á´á´ á´á´xá´á´

sá´á´á´ÊÒá´sá´ á´É´á´ ÊÉªÉ¢Ê Ç«á´á´ÊÉªá´Ê á´ á´ á´á´sÉªá´

á´Êá´Êá´Ê Êá´á´ á´Êá´á´á´á´á´ ÊÊ [AÊÊÉªá´á´É´Êá´ SÉªÉ´É¢Ê Rá´É´á´á´¡á´á´](https://t.me/Venom_Hai_Hum)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â°ðï¸ððï¸ð²ð¡ï¸â±", url="https://t.me/Sanki_Owner")
                  ],[
                    InlineKeyboardButton(
                        "â°á´ÊÉªê±Êá´âá´Êá´Êá´Ê ðá´á´á´á´Æ¦á´â±", url="https://t.me/EsportClan"
                    ),
                    InlineKeyboardButton(
                        "â°á´ÊÉªê±Êá´âá´Êá´Êá´Ê É¢Æ¦á´á´á´â±", url="https://t.me/Prayagraj_Op"
                    )
                ],
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ð ððð¶ð° ðð¼ð ð¢ð»ð¹ð¶ð»ð² ð¡ð¼ð\nð â°á´ÊÉªê±Êá´âá´Êá´Êá´Êâ±<3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¼ðá´á´á´á´Æ¦á´", url="https://t.me/AlishaSupport")
                ]
            ]
        )
   )
