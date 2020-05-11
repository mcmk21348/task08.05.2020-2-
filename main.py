#!venv/bin/python3.8
import config
import telebot


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat_id, f, None)


@bot.message_handler(content_types=['text'])
def reapeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)



if __name__ == '__main__':
    bot.infinity_polling()