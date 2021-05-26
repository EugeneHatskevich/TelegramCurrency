from telegram import Update
from telegram.ext import CallbackContext
from bd_functions.function import get_currency_by_code
from keyboard import create_keyboard
from config import MENU, INFO, CONVERTER, CONVERTER_SECOND, CONVERTER_END
from source.keyboard_list import main_button_for_info, main_button_for_converter
from create_button_list import create_button_list


def menu(update: Update, context: CallbackContext):
    update.callback_query.edit_message_text(
        text="Выберите",
        reply_markup=create_keyboard({'info': 'Курсы валют',
                                      'converter': 'Конвертер валют'})
    )
    return INFO


def info(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'info':
        buttons = create_button_list(True, main_button_for_info)
        buttons['other'] = 'Другие...'
        update.callback_query.edit_message_text(text="Выберите валюту",
                                                reply_markup=create_keyboard(buttons))
        return INFO

    elif query.data == 'other':
        other_buttons = create_button_list(False, main_button_for_info)
        other_buttons['info'] = 'Вернуться назад'
        update.callback_query.edit_message_text(text="Выберите валюту",
                                                reply_markup=create_keyboard(other_buttons))
        return INFO

    else:
        code = query.data
        currency = get_currency_by_code(code)
        count = currency.count
        value = currency.value
        answer = f'{count} {code} = {value} руб.'
        update.callback_query.edit_message_text(text=answer,
                                                reply_markup=create_keyboard({'menu': 'Вернуться в меню'}))
        return MENU


def converter(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'converter':
        buttons = create_button_list(True, main_button_for_converter)
        buttons['converter_other'] = 'Другие...'
        update.callback_query.edit_message_text(text="Выберите первую валюту",
                                                reply_markup=create_keyboard(buttons))
        return CONVERTER

    elif query.data == 'converter_other':
        other_buttons = create_button_list(False, main_button_for_converter)
        other_buttons['converter'] = 'Вернуться назад'
        update.callback_query.edit_message_text(text="Выберите первую валюту",
                                                reply_markup=create_keyboard(other_buttons))
        return CONVERTER

    else:
        first = query.data
        context.user_data['First'] = first
        buttons = create_button_list(True, main_button_for_converter)
        buttons['converter_other'] = 'Другие...'
        update.callback_query.edit_message_text(text="Выберите вторую валюту",
                                                reply_markup=create_keyboard(buttons))
        return CONVERTER_SECOND


def converter_second(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'converter':
        buttons = create_button_list(True, main_button_for_converter)
        buttons['converter_other'] = 'Другие...'
        update.callback_query.edit_message_text(text="Выберите вторую валюту",
                                                reply_markup=create_keyboard(buttons))
        return CONVERTER_SECOND

    elif query.data == 'converter_other':
        other_buttons = create_button_list(False, main_button_for_converter)
        other_buttons['converter'] = 'Вернуться назад'
        update.callback_query.edit_message_text(text="Выберите вторую валюту",
                                                reply_markup=create_keyboard(other_buttons))
        return CONVERTER_SECOND

    else:
        second = query.data
        context.user_data['Second'] = second
        update.callback_query.edit_message_text(text='Введите количество конвертируемой валюты')

        return CONVERTER_END


def other(update: Update, context: CallbackContext):
    update.callback_query.edit_message_text(text='Произошел перезапуск, просьба начать с команды "/start"')
