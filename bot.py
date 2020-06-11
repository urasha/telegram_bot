import telebot
from telebot import types

bot = telebot.TeleBot('1203791454:AAEFCUHK-e0vfvHgpsjngvmKj8hl20YfFhA')


def start_game(message_):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Rock', 'Scissors', 'Paper')

    bot.send_message(message_.from_user.id, 'Make you choice: ', reply_markup=keyboard)


def show_result():
    


@bot.message_handler(content_types=['text'])
def send_fail(message):
    if message.text == '/game':
        start_game(message)

    elif message.text.lower() in ['rock', 'scissors', 'paper']:
        show_result()

    else:
        bot.send_message(message.from_user.id, 'Type /game to start')


bot.polling(none_stop=True)
