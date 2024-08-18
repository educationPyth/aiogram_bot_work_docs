from aiogram import Bot
from aiogram.types import Message, FSInputFile, CallbackQuery
from core.keyboards.inlins import *

async def get_start(message: Message, bot: Bot):
    chat_id = message.from_user.id
    await bot.send_message(chat_id,f'🤝 Привет!!! 🤝\n'
                                   f'Этот бот finlogistika_bot"\n'
                                   )

