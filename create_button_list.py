from bd_functions.function import get_all_currency


def create_button_list(in_list: bool, button_list: list) -> dict:
    all_currency = get_all_currency()
    buttons = {}
    for currency in all_currency:
        if in_list:
            if currency.name in button_list:
                buttons[currency.code] = f'{currency.count} {currency.name}'
        else:
            if currency.name not in button_list:
                buttons[currency.code] = f'{currency.count} {currency.name}'
    return buttons
