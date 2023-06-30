import telebot
from PIL import Image
import os

chave_api = 'SEU_TOKEN' # Preencha com o token fornecido pelo BotFather

bot = telebot.TeleBot(chave_api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Estou pronto! Envie a foto')

@bot.message_handler(content_types=['sticker', 'document', 'audio', 'PPM', 'SGI', 'TGA', 'WEBP'])
def received_photo(message):
    bot.reply_to(message, 'Me envie uma foto!')

@bot.message_handler(content_types=['photo'])
def download_image(message):
    chat_id = message.chat.id
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    
    bot.reply_to(message, '''
Clique no formato desejado:
/png -  PNG
/ico -  ICON
/pdf -  PDF
/jpg -  JPEG
/tiff - TIFF
/bmp -  BMP
/dib -  DIB
/eps -  EPS
/im -   IM
/pcx -  PCX
/ppm -  PPM
/sgi -  SGI
/tga -  TGA
/webp - WEBP
    ''')


@bot.message_handler(commands=['png', 'ico', 'pdf', 'jpg', 'tiff', 'bmp', 'dib', 'eps', 'im', 'pcx', 'ppm', 'sgi', 'tga', 'webp'])
def convert_to_png(message):
    chat_id = message.chat.id
    format_command = message.text[1:]
    format_name = format_command.upper()
    output_path = f"image.{format_name.lower()}"
    
    try:
        image = Image.open("image.jpg")
        image.save(output_path, format=format_name)
        
        with open(output_path, 'rb') as file:
            bot.send_document(chat_id, file)
        
        delete_image("image.jpg")
        delete_image(output_path)
    except Exception as e:
        bot.reply_to(message, f"Erro ao converter a imagem para {format_name}: {str(e)}")

def delete_image(file_path):
    try:
        os.remove(file_path)
        print(f"Imagem {file_path} removida com sucesso.")
    except Exception as e:
        print(f"Erro ao remover a imagem {file_path}: {str(e)}")

bot.polling()