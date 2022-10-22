import telebot
import time
from threading import Thread
from loguru import logger
from chat_helpers import Chat, Container, literal_days

bot = telebot.TeleBot('5421439498:AAGppFxe-rh_WTM5SUEGJmtLiPMCd20_SJo')

members = Container()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global members
    members.update(Chat(message.chat.id))

    chat = members.get(message.chat.id)
    if message.text == "/count":
        if chat.time_delta.days == 0:
            bot.send_message(
                message.chat.id,
                f"Ты бы притормозил, судя по таймеру ты заливался меньше одного дня назад",
            )
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEGLBFjVGJ76EOHLXzJiRSNb-ywZD19IAACkgEAAonq5QcjCcbKL6NW8yoE')
        else:
            bot.send_message(
                message.chat.id,
                f"Ты не был в Right Hops уже {chat.time_delta.days} {literal_days(chat.time_delta.days)} :(((",
            )

    elif message.text == "/check_in":
        for mem in members.members:
            if message.chat.id == mem.id:
                mem.check_in()
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEGLBNjVGKjmz7Z42HqBHARpIdwBt-twQACbQEAAonq5QeQ9Vt1jHr5yyoE')
        bot.send_message(message.chat.id, "Здарова, заебал")
        bot.send_message(message.chat.id, f"Время попойки: {members.get(message.chat.id).check_in_time}")
        time.sleep(1)
        bot.send_message(message.chat.id, "Не забудь заказать похавоть, чеб не разъебало раньше времени")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Счетчик того, сколько ты уже не захаживал в Right Hops")
        time.sleep(1)
        bot.send_message(message.chat.id, "Если хочешь узнать, сколько ты продержался без невъебенного вкуса пива с картошечкой, хуярь /count")
        time.sleep(1)
        bot.send_message(message.chat.id, "Если ты красавчик и сейчас хуяришь пиво в любимом барчике, хуярь /check_in")
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGLA9jVGJepCTY2pXMvGTwo2ZjivZ_mQACTAEAAonq5QcmOMdrO1Q6TSoE')
        bot.send_message(message.chat.id, "Заебал, нихуя не понятно, жмакни /help.")


def _counter():
    while True:
        for mem in members.members:
            mem.calc_delta()


def start():
    threads = [
        Thread(target=_counter),
    ]
    for th in threads:
        th.start()

    logger.info('Бот запущен')
    bot.polling(none_stop=True, interval=1)
    logger.info('Бот здох')
