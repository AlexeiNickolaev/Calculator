import datetime


def log_cash(some_str, result):
    path = 'calculator\log.txt'
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'{some_str} = {result}. Время запроса: {str(datetime.datetime.now())} \n')