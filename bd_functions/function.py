from parsing.parse import parse
from config import URL
from models.bd_connection import *
from typing import List


def get_all_currency() -> List[Currency]:
    """Получить все курсы валют"""
    list_currency = Currency.select()
    return list_currency


def get_currency_by_code(code: str) -> Currency:
    """Получить значение курса по коду валюты"""
    currency = Currency.get(Currency.code == code)
    return currency


def create_data():
    """ Создание таблицы """
    data = parse(URL)
    for i in data:
        create_currency(i,
                        int(data[i]['Количество и код страны'].split(' ')[0]),
                        data[i]['Количество и код страны'].split(' ')[1],
                        float(data[i]["Официальный курс"].replace(',', '.')))


def create_currency(name: str, count: int, code: str, value: float):
    row = Currency.create(name=name.strip(),
                          count=count,
                          code=code,
                          value=value)
    row.save()


def update_data():
    """ Обновление данных """
    data = parse(URL)
    for i in data:
        update_currency(i,
                        int(data[i]['Количество и код страны'].split(' ')[0]),
                        float(data[i]["Официальный курс"].replace(',', '.')))


def update_currency(name: str, count: int, value: float):
    Currency.update(count=count,
                    value=value,
                    updated_at=datetime.datetime.now()).where(Currency.name == name).execute()
