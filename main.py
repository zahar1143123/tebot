from telebot import *
from webbrowser import *

bot = TeleBot('6087747134:AAHAfqb26G2t6BZzHzOhaNgbmjJkou_DmQ4')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('go to site', url='https://www.google.com/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Edit photo', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Fantastic Photo !', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edited' ,callback.message.chat.id, callback.message.message_id )


@bot.message_handler(commands=['site', 'website'])
def site(message):
    open('https://www.youtube.com/')

@bot.message_handler(commands=['start', 'hi', 'hello'])
def main(message):
    bot.send_message(message.chat.id,  f'Hi, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help information</b> \n <em>/start - start</em> \n /hi or /hello - sayhello', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id,  f'Hi, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.infinity_polling()