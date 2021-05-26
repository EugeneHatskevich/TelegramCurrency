import requests


def parse(url):
    """Возвращает словарь с данными по курсам валют"""
    html: list = requests.get(url).json()
    html.append({'Cur_ID': 777,
                 'Date': '2021-05-26T00:00:00',
                 'Cur_Abbreviation': 'BYN',
                 'Cur_Scale': 1,
                 'Cur_Name': 'Белорусский рубль',
                 'Cur_OfficialRate': 1.00000})
    return html
