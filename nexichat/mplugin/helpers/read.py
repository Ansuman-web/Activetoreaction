from config import OWNER_USERNAME, SUPPORT_GRP
from nexichat import nexichat
from pyrogram import Client, filters



START = """**
{} ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴄʜᴀᴛʙᴏᴛ 

➪ ꜱᴜᴘᴘᴏʀᴛꜱ ᴛᴇxᴛ, ꜱᴛɪᴄᴋᴇʀ, ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ...
➪ ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ 
➪ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ 
➪ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ᴄʜᴀᴛʙᴏᴛ 
➪ ᴍᴀᴋᴇ ʏᴏᴜʀ ɪᴅ-ᴄʜᴀᴛʙᴏᴛ 


╔═══⋆ʟᴏᴠᴇ ᴡɪᴛʜ⋆═══╗
★ [⎯꯭֯🖤⃪ ꯭⃛֯ ̶̲̽͟𓆩⃪ͥ͢ ᷟ𓆩𝙍𝘼𝘿𝙃𝙀 ⃪𝄀꯭𝄄꯭ا✾༐𓂃⃪꯭,, ㅤ ™](https://t.me/ll_BOTCHAMBER_ll)     ★
╚═════ ⋆★⋆ ═════╝
**"""

HELP_READ = f"""**
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/ur_rishu_143).

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**
"""

TOOLS_DATA_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴛᴏᴏʟꜱ:

➻ /start ᴛᴏ ᴡᴀᴋᴇ ᴜᴘ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ʀᴇᴄᴇɪᴠᴇ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ!
──────────────
➻ /help ғᴏʀ ɢᴇᴛᴛɪɴɢ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs.
──────────────
➻ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ (ᴘɪɴɢ) ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➻ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ, ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴏɴᴇ ᴍᴇssᴀɢᴇ.
──────────────
➻ /broadcast ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄʜᴀᴛs ʙᴀsᴇᴅ ᴏɴ sᴘᴇᴄɪғɪᴇᴅ ғʟᴀɢs!\nᴇxᴀᴍᴘʟᴇ: `/broadcast -user -pin ʜᴇʟʟᴏ ғʀɪᴇɴᴅs`
──────────────
➻ /shayri ɢᴇᴛ ʀᴀɴᴅᴏᴍ sʜᴀʏʀɪ ғᴏʀ ʏᴏᴜʀ ʟᴏᴠᴇ
──────────────
➻ /link (ɢʀᴏᴜᴩ ɪᴅ) ᴛᴏ ɢᴇᴛ ʟɪɴᴋ ᴏꜰ ɢʀᴏᴜᴩ
➻ /givelink ᴛᴏ ɢᴇᴛ ᴛʜᴀᴛ ɢʀᴏᴜᴩ ʟɪɴᴋ ɪɴ ᴡʜɪᴄʜ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴡʀɪᴛᴛᴇɴ (ᴡʀɪᴛᴇ ɪɴ ɢʀᴏᴜᴩ)
──────────────


╔═══⋆ʟᴏᴠᴇ ᴡɪᴛʜ⋆═══╗
★[⎯꯭֯🖤⃪ ꯭⃛֯ ̶̲̽͟𓆩⃪ͥ͢ ᷟ𓆩𝙍𝘼𝘿𝙃𝙀 ⃪𝄀꯭𝄄꯭ا✾༐𓂃⃪꯭,, ㅤ ™](https://t.me/ll_BOTCHAMBER_ll)    ★
╚═════ ⋆★⋆ ═════╝ **
"""

CHATBOT_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴄʜᴀᴛʙᴏᴛ:

➻ /chatbot - ᴏᴘᴇɴs ᴏᴘᴛɪᴏns ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.
──────────────
➻ /ask - ᴀꜱᴋ ᴀɴʏᴛʜɪɴɢ ꜰʀᴏᴍ ᴄʜᴀᴛɢᴩᴛ
──────────────
➻ /lang, /language, /setlang - ᴏᴘᴇɴs ᴀ ᴍᴇɴᴜ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ.  
──────────────
➻ /resetlang, /nolang - ʀᴇsᴇᴛs ᴛʜᴇ ʙᴏᴛ's ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ ᴍɪxᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
──────────────
➻ /chatlang - ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ᴜꜱɪɴɢ ᴄʜᴀᴛ ʟᴀɴɢ ꜰᴏʀ ᴄʜᴀᴛ.
──────────────
➻ /status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ ᴀᴄᴛɪᴠᴇ ᴏʀ ɴᴏᴛ.
──────────────
➻ /stats - ɢᴇᴛ ʙᴏᴛ ꜱᴛᴀᴛꜱ
──────────────
➻ /clone [ ʙᴏᴛ ᴛᴏᴋᴇɴ ] - ᴛᴏ ᴄʟᴏɴᴇ ʏᴏᴜʀ ʙᴏᴛ.
──────────────
➻ /idclone [ ᴩʏʀᴏɢʀᴀᴍ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ] - ᴛᴏ ᴍᴀᴋᴇ ɪᴅ-ᴄʜᴀᴛʙᴏᴛ.
──────────────


╔═══⋆ʟᴏᴠᴇ ᴡɪᴛʜ⋆═══╗
★[⎯꯭֯🖤⃪ ꯭⃛֯ ̶̲̽͟𓆩⃪ͥ͢ ᷟ𓆩𝙍𝘼𝘿𝙃𝙀 ⃪𝄀꯭𝄄꯭ا✾༐𓂃⃪꯭,, ㅤ ™](https://t.me/ll_BOTCHAMBER__ll)     ★
╚═════ ⋆★⋆ ═════╝**
"""

SOURCE_READ = f"**❍ ʜᴇʏ, ᴛʜᴇ [{nexichat.name}](https://t.me/{nexichat.username}) ɪs ɴᴇᴡ ᴘᴏᴡᴇʀғᴜʟʟ ᴄʜᴀᴛʙᴏᴛ ᴏғ ᴡʜᴏʟᴇ ᴛᴇʟᴇɢʀᴀᴍ.**\n\n**❍ ᴘʟᴇᴀsᴇ ᴅᴏɴᴀᴛᴇ ᴛʜᴇ ᴅᴇᴠʟᴏᴘᴇʀ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴ ᴛʜᴇ ᴘʀᴏɪᴇᴄᴛs**\n\n**⦿──────────────────⦿**\n\n**⦿──────────────────⦿**\n\n**❍ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_GRP})..\n\n<b>||❍ ʟᴏᴠᴇ ᴡɪᴛʜ ➪ [⎯꯭֯🖤⃪ ꯭⃛֯ ̶̲̽͟𓆩⃪ͥ͢ ᷟ𓆩𝙍𝘼𝘿𝙃𝙀 ⃪𝄀꯭𝄄꯭ا✾༐𓂃⃪꯭,, ㅤ ™](https://t.me/ll_BOTCHAMBER_ll) **||</b>"

ADMIN_READ = f"sᴏᴏɴ"

ABOUT_READ = f"""
**➻ [{nexichat.name}](https://t.me/{nexichat .username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**

**➻ [{nexichat.name}](https://t.me/{nexichat.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**

**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**

**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**

**──────────────**

**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{nexichat.name}](https://t.me/{nexichat.username})**
"""
