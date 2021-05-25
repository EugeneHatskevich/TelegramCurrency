from telegram import Update
from telegram.ext import CallbackContext
from bd_functions.function import get_currency_by_code
from keyboard import create_keyboard
from config import MENU, CONVERTER_END
from converter import converter
from validation.value_validation import value_validation


def convert_end(update: Update, context: CallbackContext):
    first_currency_code = context.user_data['First']
    second_currency_code = context.user_data['Second']
    value = update.message.text
    is_float_value = value_validation(value)
    if is_float_value:
        first_currency = get_currency_by_code(first_currency_code)
        second_currency = get_currency_by_code(second_currency_code)
        result = converter(first_currency, second_currency, float(value))
        update.message.reply_text(text=result)
        update.message.reply_text(text='Вернуться в меню',
                                  reply_markup=create_keyboard({'menu': 'Вернуться в меню'}))
        return MENU
    else:
        update.message.reply_text(text='Введите верное значение!!!', )
        return CONVERTER_END
