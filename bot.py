import discord
import settings
import time
from discord.ext import commands

client = commands.Bot(command_prefix = settings.PREFIX, self_bot = True)

print_messages = [
	'I am ready! Just send .start in chat.',
	'Are you ready? (y/n) ', 
	'Write text there. To finish just press Enter ', 
	'Write count of repeat ',
	'Write time interval between messages (s) ',
	'y',
	'n',
]

if settings.LANGUAGE == "ru":
	print_messages = [
		'Теперь чтобы запустить бота введите .start в чате',
		'Вы готовы? (д/н) ',
		'Введите текст для отправки здесь. Чтобы закончить ввод нажмите Enter ',
		'Введите количество повторений ',
		'Введите интервал между сообщениями (c) ',
		'д',
		'н',
	]

@client.event
async def on_ready():
	print(print_messages[0])

isReady = ''
while isReady != print_messages[5]:
	isReady = input(print_messages[1])

newMessage = str(input(print_messages[2]))
text = []
while newMessage != '':
	text.append(newMessage)
	newMessage = str(input(print_messages[2]))

repeatCount = 0
while repeatCount == 0:
	x = int(input(print_messages[3]))

	if x>=1:
		repeatCount = x

sleepTime = int(input(print_messages[4]))

if (isReady == print_messages[5] and text!=''):
	@client.command()
	async def start(ctx, messages = text, count = repeatCount, wait = sleepTime):
		for i in range(count):
			for message in messages:
				await ctx.send(message)
				time.sleep(wait)
			time.sleep(wait)

client.run(settings.TOKEN, bot = False)