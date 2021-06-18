from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello 👋 there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n🔴 Do you want me to play music in your Telegram groups'voice chats? Please click the \'📃 User Manual 📃\' button below to know how you can use me.\n\n🔴 The Assistant must be in your group to play music in the voice chat of your group.\n\n🔴 More info & commands mentioned in the [User Manual](https://telegra.ph/file/d5f0ee06089ac31379a19.jpg)\n\nA project by @Darkridersslk\n Join Our Group @joingrouplk""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📃 User Manual 📃", url="https://telegra.ph/file/d5f0ee06089ac31379a19.jpg")
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻 Updates 👨‍💻", url="https://t.me/Ezila_Updates"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Chat 🎙️", url="https://t.me/Ezila_Support"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/Ezila_Support")
                ]
            ]
        )
   )
