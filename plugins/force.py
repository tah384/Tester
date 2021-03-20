async def incoming_start_message_f(bot, update): """/start command""" if not await db.is_user_exist(update.chat.id): await db.add_user(update.chat.id) update_channel = UPDATES_CHANNEL if update_channel: try: user = await bot.get_chat_member(update_channel, update.chat.id) if user.status == "kicked": await bot.send_message( chat_id=update.chat.id, text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/VKP_BOTS).", parse_mode="markdown", disable_web_page_preview=True ) return except UserNotParticipant: await bot.send_message( chat_id=update.chat.id, text="**Please Join My Updates Channel to use this Bot!**", reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{update_channel}") ] ] ), parse_mode="markdown" ) return except Exception: await bot.send_message( chat_id=update.chat.id, text="Something went Wrong. Contact my [Support Group](https://t.me/VKP_BOTS).", parse_mode="markdown", disable_web_page_preview=True)
