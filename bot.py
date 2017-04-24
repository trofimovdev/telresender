# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


	
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, 'Работаю 24 часа, 7 дней в неделю, 365 дней в году. \n\nНапиши /help для помощи.')

@bot.message_handler(commands=["help"])
def start(message):
	bot.send_message(message.chat.id, 'Как пользоваться? Очень просто. \n\nПросто отправь мне сообщение, а когда мой хозяин ответит, я автоматически перешлю его тебе. \n\n Ах, да. Если ты мне ничего не напишешь, то я ничего ему не отправлю😈')







@bot.message_handler(content_types=["text"])
def messages(message):
	if int(message.chat.id) == int(config.owner):
		try:
			chatId=message.text.split(': ')[0]
			text=message.text.split(': ')[1]
			bot.send_message(chatId, text)
		except:
			pass
	else:
		bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
		bot.send_message(message.chat.id, '%s, Ваш запрос принят. Bastax уже получил его. Ожидайте 👍'%message.chat.username)

if __name__ == '__main__':
	bot.polling(none_stop=True)
