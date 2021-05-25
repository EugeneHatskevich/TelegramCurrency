from models.bd_connection import Currency


def converter(first_currency: Currency, second_currency: Currency, value: float) -> str:
    first_currency_count = int(first_currency.count)
    second_currency_count = int(second_currency.count)
    first_currency_value = float(first_currency.value)
    second_currency_value = float(second_currency.value)
    converter_result = value * first_currency_value * second_currency_count / first_currency_count / second_currency_value
    answer = f'{value} {first_currency.code} = {round(converter_result, 2)} {second_currency.code}'
    return answer
