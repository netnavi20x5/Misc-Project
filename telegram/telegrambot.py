import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	print ('Command received: %s' % command)

	if command == '/about':
		bot.sendMessage(chat_id, 'Hello world')
		bot.sendMessage(chat_id, 'Hello world2')
		bot.sendMessage(chat_id, 'Hello world3')
	elif command == '/random':
		bot.sendMessage(chat_id, random.randint(0,9))
	elif command == '/time':
		bot.sendMessage(chat_id, str(datetime.datetime.now()))
	elif command == 'hello':
		bot.sendMessage(chat_id, 'Hello world')

bot = telepot.Bot('BOT KEY')

MessageLoop(bot, handle).run_as_thread()
print ('Bot ready!')

while 1:
	time.sleep(10)
