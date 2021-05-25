from bs4 import BeautifulSoup


def get_content(html: str):
    """Возвращает словарь с данными по курсам валют"""
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr')
    course = {}
    for item in items[1:]:
        course[item.find('span', class_='text').get_text()] = {
            'Количество и код страны': item.find('td', class_='curAmount').get_text(),
            'Официальный курс': item.find('td', class_='curCours').find('div').get_text()
        }
    course['Белорусский рубль'] = {
        'Количество и код страны': '1 BYN',
        'Официальный курс': '1,000'
    }
    return course
