import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handler import router


async def main():
    bot = Bot(token="6702587206:AAEPfBKkSepilgjyPKOesnL_X8cXx-CTXII")
    dp = Dispatcher(storage=MemoryStorage())
    logging.basicConfig(level=logging.INFO)
    dp.include_routers(router)
    await dp.start_polling(bot, dp=dp)

if __name__ == '__main__':
    asyncio.run(main())