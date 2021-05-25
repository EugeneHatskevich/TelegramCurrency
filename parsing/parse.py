from .get_content import get_content
import requests


def parse(url):
    """Возвращает словарь с данными по курсам валют"""
    html = requests.get(url).text
    courses = get_content(html)
    return courses
