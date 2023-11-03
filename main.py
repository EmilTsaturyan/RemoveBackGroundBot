import telebot
from removebg import RemoveBackGround
from PIL import Image

bot = telebot.TeleBot("BOT TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello🖐️, this bot can remove background from your image just sent it.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Send the image and bot will remove the background of the image')

@bot.message_handler(content_types=['photo'])
def get_broadcast_picture(message):
    bot.send_message(message.chat.id, 'Working on it!')
    file_path = bot.get_file(message.photo[-1].file_id).file_path
    file = bot.download_file(file_path)
    with open('images/input.jpg', 'wb') as code:
        code.write(file)
    
    rb = RemoveBackGround('images/input.jpg', 'images/output.png')
    rb.remove_bg()
    image = Image.open('images/output.png')
    bot.send_photo(message.chat.id, image)
    
bot.infinity_polling()
