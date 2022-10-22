import telebot
import time
from threading import Thread
from loguru import logger

bot = telebot.TeleBot('5421439498:AAGppFxe-rh_WTM5SUEGJmtLiPMCd20_SJo')
start_time = time.perf_counter()
delta_sec = 0

members_id = set()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global start_time
    global members_id
    members_id.add(message.from_user.id)

    if message.text == "/count":
        bot.send_message(message.from_user.id, "Ты не был в Right Hops уже %.3f секунд :(((" % delta_sec)
    elif message.text == "/check_in":
        start_time = time.perf_counter()
        bot.send_message(message.from_user.id, "Здарова, заебал")
        time.sleep(3)
        bot.send_message(message.from_user.id, "Не забудь заказать похавоть, чеб не разъебало раньше времени")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Счетчик того, сколько ты уже не захаживал в Right Hops")
        time.sleep(1)
        bot.send_message(message.from_user.id, "Если хочешь узнать, сколько ты продержался без невъебенного вкуса пива с картошечкой, хуярь /count")
        time.sleep(1)
        bot.send_message(message.from_user.id, "Если ты красавчик и сейчас хуяришь пиво в любимом барчике, хуярь /check_in")
    else:
        bot.send_message(message.from_user.id, "Заебал, нихуя не понятно, жмакни /help.")


def _counter():
    global delta_sec
    while True:
        delta_sec = time.perf_counter() - start_time


def _vzdrachivatel():
    t0 = time.perf_counter()
    while True:
        if time.perf_counter() - t0 > 86400:
            t0 = time.perf_counter()
            for mem in members_id:
                bot.send_message(mem, "ТЫ ПИДОР")


def start():
    threads = [
        Thread(target=_counter),
        Thread(target=_vzdrachivatel),
    ]
    for th in threads:
        th.start()

    logger.info('Бот запущен')
    bot.polling(none_stop=True, interval=1)
    logger.info('Бот здох')
