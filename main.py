
import logging
import requests
import pandas as pd
import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv('TOKEN')
CHAT_ID = 'chat_id_خودت_اینجا (اختیاری)'

def get_sample_stock_data():
    data = {
        'شستا': {'قیمت': 1230, 'تغییر': '+1.2%'},
        'فولاد': {'قیمت': 2540, 'تغییر': '-0.6%'},
        'خودرو': {'قیمت': 1780, 'تغییر': '+0.9%'}
    }
    return data

def send_report(context):
    data = get_sample_stock_data()
    message = 'گزارش روزانه بورس:\n'
    for name, info in data.items():
        message += f"\n{name}: {info['قیمت']} تومان ({info['تغییر']})"
    context.bot.send_message(chat_id=CHAT_ID, text=message)

def start(update, context):
    update.message.reply_text('ربات تحلیلگر بورس فعال شد.')

def main():
    logging.basicConfig(level=logging.INFO)
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    job = updater.job_queue
    job.run_repeating(send_report, interval=3600, first=5)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
