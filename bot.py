# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config
API_ID = '20268266'
API_HASH = '924217707ae50aaf7cd46144db729ae8'
BOT_TOKEN = '7068430796:AAF7iun7-R4AeXrY6GwNwi8cpwhfsWuo0Z8'

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.API_ID, 
    api_hash=Config.API_HASH, 
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
