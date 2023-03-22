import os
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_correct_year_ending(year):
    last_two_digits = year % 100
    tens = last_two_digits // 10
    if tens == 1:
        return 'лет'
    ones = last_two_digits % 10
    if ones == 1:
        return 'год'
    if 2 <= ones <= 4:
        return 'года'
    return 'лет'


def get_wine(excel):
    drinks = pd.read_excel(excel, na_values='None', keep_default_na=False)
    drinks_aggregated = drinks.groupby("Категория").apply(lambda wine: wine.to_dict(orient="records")).to_dict()
    return drinks_aggregated


def main():
    load_dotenv()
    excel_wine = os.getenv('EXCEL_PATH')
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    current_year = datetime.now().year
    established_year = datetime(year=1920, month=1, day=1).year
    years_delta = current_year - established_year

    rendered_page = template.render(
        winery_age=f'{years_delta} {get_correct_year_ending(years_delta)}',
        drinks=get_wine(excel_wine)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8001), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
