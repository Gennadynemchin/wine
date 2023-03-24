# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

```git clone https://github.com/Gennadynemchin/wine.git```
- Создайте виртуальное окружение:
```
python -m venv env
```
- Активируйте (Mac/Linux):
```
source env/bin/activate
```
- Win:
```
env\Scripts\activate.bat
```
Установите зависимости:
```
pip install -r requirements.txt
```
- Скопируйте excel файл в корень проекта. В проекте уже есть пример файла - 
```wine_example.xlsx```. Вы можете запустить сайт с ним.
- пропишите имя excel файла в ```.env.example.``` или оставьте имеющийся сэмпл. Перед запуском необходимо
переименовать ```.env.example``` в ```.env```. Пример содержимого файла ```.env```:
```
EXCEL_PATH='<NAME_OF_xlsx_IN_CURRENT_DIRECTORY>'
```


- Запустите сайт:
```
python main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8001](http://127.0.0.1:8001)


