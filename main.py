from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

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


current_year = datetime.now().year
established_year = datetime(year=1920, month=1, day=1).year
years_delta = current_year - established_year

rendered_page = template.render(
    winery_age=f'{years_delta} {get_correct_year_ending(years_delta)}'
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8001), SimpleHTTPRequestHandler)
server.serve_forever()
