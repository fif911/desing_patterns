"""
https://tproger.ru/translations/demystifying-decorators-in-python/

Декораторы не обязательно должны быть функциями, это может быть любой вызываемый объект.
Декораторы не обязаны возвращать функции, они могут возвращать что угодно. Но обычно мы хотим, чтобы декоратор вернул объект того же типа, что и декорируемый объект. Пример:
"""


def benchmark(func):
    #  Декоратор принимает функцию в качестве аргумента и возвращает функцию

    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


# def fetch_webpage(): Мы можем обвернуть функцию так которая и принимает параметры. Так и без параметров
# так же у самих декоратора могут быть параметры
# @benchmark(iters=10)
@benchmark
def fetch_webpage(url):  # у функиций которые мы обворачиваем в декоратор могут быть параметры
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)
