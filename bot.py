import os
from datetime import date
import telepot
from send2trash import send2trash
from telepot.loop import MessageLoop
from dotenv import load_dotenv
import logging


logging.basicConfig(filename='ArchivalBot.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
load_dotenv()  
API_KEY = os.getenv("API_KEY")
CHAT_ID = os.getenv("CHAT_ID")
ARCHIVE_FILE_PATH = os.getenv("ARCHIVE_FILE_PATH")


def handle():
    os.chdir(ARCHIVE_FILE_PATH)
    bot.sendMessage(CHAT_ID, f"Starting new arcive at {date.today()}")
    filesMissed = []
    for file in os.listdir():
        file_path = os.path.join(ARCHIVE_FILE_PATH , file)
        try:
            bot.sendDocument(chat_id=CHAT_ID, document=open(file_path, 'rb'))
        except Exception as e:
            logging.error(e)
            filesMissed.append(file)
    if filesMissed != []:
         bot.sendMessage(CHAT_ID, f"arcive at {date.today()} missed {filesMissed} check log for more info")
    else:
         bot.sendMessage(CHAT_ID, f"arcive at {date.today()} Completed Sucessfully")
    files_to_be_removed = list(set(os.listdir()) - set(filesMissed)) 
    send2trash(files_to_be_removed)
        
bot = telepot.Bot(API_KEY)
handle()