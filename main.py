from aiogram import Dispatcher, F
from aiogram.filters import Command
from core.handlers.basic import *
import asyncio
import logging
from core.settings import settings
from core.utils.commands import set_commands

dp = Dispatcher()


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!!')


async def start():
    bot = Bot(token=settings.bots.bot_token)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if hasattr(bot, 'token'):
        try:
            print('Бот работает!')
        except Exception as e:
            print(f'Призошла ошибка {e}')
    else:
        print('Бот не работает!')

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)



    try:
        await dp.start_polling(bot, parse_mode="HTML")
    except Exception as e:
        logging.error(f'Произошла ошибка: {e}')
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

