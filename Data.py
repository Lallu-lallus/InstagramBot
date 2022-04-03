from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """ʜᴇʏ {}  

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}  

ɪ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇs, ᴠɪᴅᴇᴏs, ɪᴍᴀɢᴇs ᴀɴᴅ ʀᴇᴇʟs ғʀᴏᴍ ɪɴsᴛᴀɢʀᴀᴍ ᴀʟᴏɴɢ ᴡɪᴛʜ ᴘᴏsᴛ ᴄᴀᴘᴛɪᴏɴ. ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴀᴜᴛʜᴏʀɪᴢᴇ ᴍᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀɪᴠᴀᴛᴇ ᴘᴏsᴛs.  

ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🚧", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛs 🤖", url="https://t.me/GroupDcBots/7286")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ⚡", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ 🎯", callback_data="about")
        ],
        [InlineKeyboardButton(" sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 🙈 ", url="https://t.me/Groupdc")],
    ]

    # Help Message
    HELP = """
𝟷) **ɪᴍᴀɢᴇs, ᴠɪᴅᴇᴏs ᴀɴᴅ ʀᴇᴇʟs** sᴇɴᴅ ᴛʜᴇ ʟɪɴᴋ ʜᴇʀᴇ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴘᴏsᴛ ᴄᴏɴᴛᴇɴᴛs ɪɴᴄʟᴜᴅɪɴɢ ᴄᴀᴘᴛɪᴏɴ.  

𝟸) **ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇs** ᴜsᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ `/profile_pic` ᴏʀ `/dp` ᴀʟᴏɴɢ ᴡɪᴛʜ ɪɴsᴛᴀɢʀᴀᴍ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ɢᴇᴛ ɪᴛs ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇ. ᴇxᴀᴍᴘʟᴇ : `/dp ciniedits`  

𝟹) **ᴘʀɪᴠᴀᴛᴇ ᴘᴏsᴛs** ᴀᴜᴛʜᴏʀɪᴢᴇ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀɪᴠᴀᴛᴇ ᴘᴏsᴛs. ᴜsᴇ /auth  **ɴᴏᴛᴇ** : sᴛᴏʀɪᴇs ᴀɴᴅ ɪɢᴛᴠ ᴀʀᴇ ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ.  

ᴜsᴇ /auth ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇ ᴀɴᴅ /unauth ᴛᴏ ᴜɴᴀᴜᴛʜᴏʀɪᴢᴇ.
"""

    # About Message
    ABOUT = """**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ**   

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴsᴛᴀɢʀᴀᴍ ᴄᴏɴᴛᴇɴᴛ ʙʏ @sᴛᴀʀᴋʙᴏᴛs  

sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/selfie-bd/InstagramBot)  

ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](http://docs.pyrogram.org/)  

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](http://www.python.org/)  

ᴅᴇᴠᴇʟᴏᴘᴇʀ : @GroupDcBots
    """
