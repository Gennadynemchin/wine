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
- Скопируйте excel файл в корень проекта. В проекте есть пример файла - 
```wine_example.xlsx```
- пропишите имя excel файла в ```.env.example.``` Перед запуском необходимо
переименовать ```.env.example``` в ```.env```
- Запустите сайт:
```
python main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8001](http://127.0.0.1:8001)


