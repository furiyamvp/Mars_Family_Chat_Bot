from aiogram import executor
import middlewares, handlers
from loader import dp


async def on_startup(dispatcher):
    print("Bot ishga tushdi!")


async def on_shutdown(dispatcher):
    print("Bot to'xtadi!")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
