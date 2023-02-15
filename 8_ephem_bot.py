"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
# import ephem

from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler, MessageHandler, filters

import config

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


async def reply_planet(update, context):
    #logging.INFO('The command was get: /planet')
    #ephem.constellation("Earth")
    user_text = update.message.text
    await update.message.reply_text(f'{user_text.split(" ")[1]}')

async def talk_to_me(update, context):
    user_text = update.message.text
    #logging.INFO(user_text)
    await update.message.reply_text(user_text)

def main() -> None:
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("planet", reply_planet))
    app.add_handler(MessageHandler(filters.TEXT, talk_to_me))
    logging.info('Bot was started')
    app.run_polling()

if __name__ == "__main__":
    main()
