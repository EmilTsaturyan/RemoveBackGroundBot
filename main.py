import telebot
from removebg import RemoveBackGround
from PIL import Image

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """🌟"" Welcome to the Background Remover Bot! 🌟

I'm here to help you easily remove the background from your images. Simply send me a photo, and I'll work my magic! ✨

Here's how it works:
1. Send me a photo with a clear subject you want to keep.
2. Wait a moment while I process the image.
3. Voilà! I'll send you back the image with the background removed.

Please keep in mind:
- For best results, use high-resolution images with a distinct subject.
- I don't store or share any of your images.

Feel free to give it a try! Send me an image and let's get started. If you have any questions, just type 'help'.

Enjoy using the Background Remover Bot! 📸✨
""")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, """🤖 **Background Remover Bot Help** 🤖

Need some assistance? No problem! Here are some commands you can use:

- **/help**: Display this help message.
- **/start**: Start using the bot.

Remember these tips for the best results:
- Use high-resolution images.
- Make sure the subject is clear and distinct from the background.

If you have any other questions or need further assistance, feel free to ask!

Happy background removing! 📸✨""")

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
