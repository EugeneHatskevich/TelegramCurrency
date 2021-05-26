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
        create_currency(i['Cur_ID'],
                        i['Cur_Name'],
                        i['Cur_Scale'],
                        i['Cur_Abbreviation'],
                        i['Cur_OfficialRate'])


def create_currency(cur_id: int, name: str, count: int, code: str, value: float):
    row = Currency.create(id=cur_id,
                          name=name.strip(),
                          count=count,
                          code=code,
                          value=value)
    row.save()


def update_data():
    """ Обновление данных """
    data = parse(URL)
    for i in data:
        update_currency(i['Cur_ID'],
                        i['Cur_Scale'],
                        i['Cur_OfficialRate'])


def update_currency(cur_id: int, count: int, value: float):
    Currency.update(count=count,
                    value=value,
                    updated_at=datetime.datetime.now()).where(Currency.id == cur_id).execute()
