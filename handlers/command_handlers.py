from telegram import Update
from telegram.ext import CallbackContext
from bd_functions.function import update_data, create_data
from config import ID_ADMIN
import datetime
from pytz import timezone
from keyboard import create_keyboard
from config import MENU


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Приветствую в информационном чате о курсах валют, список команд вы можете узнать введя в чате '/help'",
        reply_markup=create_keyboard({'menu': 'Нажмите, чтобы начать'})
    )
    return MENU


def update_bd(update: Update, context: CallbackContext):
    """Команда для установления ежедневного обновления информации по курсам валют"""
    chat_id = update.message.chat_id
    if chat_id == ID_ADMIN:
        context.job_queue.run_daily(update_data,
                                    time=datetime.time(1,
                                                       0,
                                                       tzinfo=timezone('Europe/Minsk')),
                                    context=chat_id,
                                    name=f'{str(chat_id)}_update_bd')
        update.message.reply_text(
            text='Ежедневные обновления установлены',
        )
    else:
        update.message.reply_text(
            text='Неверная команда',
        )


def create_bd(update: Update, context: CallbackContext):
    """Команда для установления ежедневного обновления информации по курсам валют"""
    chat_id = update.message.chat_id
    if chat_id == ID_ADMIN:
        create_data()
        update.message.reply_text(
            text='Создано',
        )
    else:
        update.message.reply_text(
            text='Неверная команда',
        )


def done(update: Update, context: CallbackContext):
    pass


def helps(update: Update, context: CallbackContext):
    update.message.reply_text(text='Бот поможет узнать курс валют на сегодня.\nТакже бот может помочь с конвертацией '
                                   'валют.\nКоманда \'/start\' запускает бота!')
