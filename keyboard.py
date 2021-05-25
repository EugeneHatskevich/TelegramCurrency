from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def create_keyboard(dict_name_button: dict) -> InlineKeyboardMarkup:
    buttons = []
    for key in dict_name_button:
        buttons.append([InlineKeyboardButton(dict_name_button[key], callback_data=key)])
    keyboard = InlineKeyboardMarkup(buttons)
    return keyboard
