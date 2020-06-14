import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('1203791454:AAEFCUHK-e0vfvHgpsjngvmKj8hl20YfFhA')

is_gaming = False
keyboard = ''


def start_game(message_):
    """
    Prepare the game for user:
        1-st  ->  create keyboard with variants
        2-nd  ->
    """

    global is_gaming, keyboard

    is_gaming = True

    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Rock', 'Scissors', 'Paper')

    bot.send_message(message_.from_user.id, check_status(),
                     reply_markup=keyboard, parse_mode='html')


def check_result(bot_choice_, user_choice_text_):
    """
    Checks for a win, loss, or draw
    """
    if user_choice_text_ == bot_choice_:
        return f"Oh, it's <b>DRAW</b>. I chose {bot_choice_} too &#129309"

    if user_choice_text_ == 'rock' and bot_choice_ == 'paper':
        return f"Hooray, I won, it's your <b>DEFEAT</b>. I chose {bot_choice_} &#128512"

    if user_choice_text_ == 'scissors' and bot_choice_ == 'rock':
        return f"Hooray, I won, it's your <b>DEFEAT</b>. I chose {bot_choice_} &#128512"

    if user_choice_text_ == 'paper' and bot_choice_ == 'scissors':
        return f"Hooray, I won, it's your <b>DEFEAT</b>. I chose {bot_choice_} &#128512"

    else:
        return f"Huh, it's your <b>WIN</b>, bro. I chose {bot_choice_} &#128532"


def show_result(user_choice):
    """
    Calculates the game result:
        1-st  ->  bot choose an action
        2-nd  ->  send the result of the game
    """

    bot_choice = ['rock', 'scissors', 'paper'][randint(0, 2)]
    user_choice_text = user_choice.text.lower()

    bot.send_message(user_choice.from_user.id, check_result(bot_choice, user_choice_text), parse_mode='html')


def send_help_commands(message_):
    """
    Send all commands of the bot to user
    """

    bot.send_message(message_.from_user.id,
                     """
<b> 
1. /game - play "Rock-Scissors-Paper" game &#128512
2. /help - show all my commands &#10067
3. /status - show gaming status at the moment &#128694 | &#127939
</b>
""", parse_mode='html')


def check_status():
    """
    Checks whether the game is running or not
    """

    if not is_gaming:
        return "<em><b>*The game hasn't started yet* &#128694</b></em>"

    return "<em><b>*The game is in full swing* &#127939</b></em>"


@bot.message_handler(commands=['game', 'start', 'help', 'stop', 'status'])
def handle_commands(message):
    global is_gaming, keyboard

    if message.text == '/game':
        start_game(message)

    if message.text == '/start':
        bot.send_message(message.from_user.id, f'Hello, {message.from_user.username} &#128152', parse_mode='html')

        bot.send_message(message.from_user.id, f"My name is <b>LOLBOT</b>. "
                                               f"That's all my commands &#128172:", parse_mode='html')

        send_help_commands(message)

    if message.text == '/help':
        send_help_commands(message)

    if message.text == '/stop':
        is_gaming = False
        keyboard_hide = types.ReplyKeyboardRemove()

        bot.send_message(message.from_user.id, "<em><b>*The game has stopped now*</b></em>",
                         reply_markup=keyboard_hide, parse_mode='html')

    if message.text == '/status':
        bot.send_message(message.from_user.id, check_status(),
                         parse_mode='html')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() in ['rock', 'scissors', 'paper']:
        show_result(message) if is_gaming else bot.send_message(message.from_user.id,
                                                                "Start the game first, and then we'll play")

    else:
        bot.send_message(message.from_user.id, "Sorry, I don't know such commands &#128533", parse_mode='html')
        bot.send_message(message.from_user.id, 'Type /help to see all my commands &#9000', parse_mode='html')


bot.polling(none_stop=True)
