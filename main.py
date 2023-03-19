from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import pandas as pd
import pprint

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


def get_correct_year_ending(year):
    lastTwoDigits = year % 100
    tens = lastTwoDigits // 10
    if tens == 1:
        return 'лет'
    ones = lastTwoDigits % 10
    if ones == 1:
        return 'год'
    if 2 <= ones <= 4:
        return 'года'
    return 'лет'


wine_dict = pd.read_excel('wine.xlsx', na_values='', keep_default_na=False).to_dict(orient="records")
current_year = datetime.now().year
established_year = datetime(year=1920, month=1, day=1).year
years_delta = current_year - established_year

wine3_dict = pd.read_excel('wine3.xlsx', na_values='None', keep_default_na=False)
wine3_dict_agg = wine3_dict.groupby("Категория").apply(lambda wine: wine.to_dict(orient="records")).to_dict()
print(wine3_dict_agg)

rendered_page = template.render(
    winery_age=f'{years_delta} {get_correct_year_ending(years_delta)}',
    wine_dict=wine3_dict_agg
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8001), SimpleHTTPRequestHandler)
server.serve_forever()
