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
import datetime
import logging
import ephem

from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler, MessageHandler, filters

import config

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='/home/eugene/bot.log')


async def reply_planet(update, context):
    logging.info(f'The command was get: {update.message.text}')
    planet_set = {"Mercury", "Venus", "Mars", "Jupiter",
                  "Saturn", "Uranus", "Neptune", "Pluto"}
    user_input_list = update.message.text.split(" ")
    if len(user_input_list) > 1:
        user_planet = user_input_list[1]
    else:
        user_planet = None
    if user_planet in planet_set:
        planet = getattr(ephem, user_planet)
        m = planet(datetime.date.today())
        user_res = f"Planet {user_planet} is now located at " \
                   f"{ephem.constellation(m)[1]}"
    elif user_planet == None:
        user_res = "Input some name of planet after the /planet command"
    elif user_planet == "Earth":
        user_res = "You can't say where Earth is, while being located here)"
    else:
        user_res = "I can't say anything about this object"

    await update.message.reply_text(f'{user_res}')

async def talk_to_me(update, context):
    user_text = update.message.text
    logging.info(user_text)
    await update.message.reply_text("Please, input some name of planet "
                                    "after the /planet command")

def main() -> None:
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("planet", reply_planet))
    app.add_handler(MessageHandler(filters.TEXT, talk_to_me))
    logging.info('Bot was started')
    app.run_polling()

if __name__ == "__main__":
    main()
