"""
https://tproger.ru/translations/demystifying-decorators-in-python/

Декораторы не обязательно должны быть функциями, это может быть любой вызываемый объект.
Декораторы не обязаны возвращать функции, они могут возвращать что угодно. Но обычно мы хотим, чтобы декоратор вернул объект того же типа, что и декорируемый объект. Пример:
"""
import inspect


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


def fetch_webpage_raw(url):
    import requests
    webpage = requests.get(url)
    return f"200: text length {len(webpage.text)}"


# def fetch_webpage(): Мы можем обвернуть функцию так которая и принимает параметры. Так и без параметров
# так же у самих декоратора могут быть параметры
# @benchmark(iters=10)
@benchmark
def fetch_webpage(url):  # у функиций которые мы обворачиваем в декоратор могут быть параметры
    import requests
    webpage = requests.get(url)
    return f"200: text length {len(webpage.text)}"


def benchmark_with_param(iters=10):  # THIS is not decorator. This is a func that takes param and returns decorator
    # for this reason to use it we not saying just benchmark we calling it with param : benchmark(iters=10)
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@benchmark_with_param(iters=2)
def fetch_webpage_dec_params(url):
    import requests
    webpage = requests.get(url)
    return f"200: text length {len(webpage.text)}"


if __name__ == '__main__':
    decorated_func = benchmark(fetch_webpage_raw)  # by fact wrapper function
    webpage = decorated_func('https://google.com')  # calling wrapper func with *args and **kwargs
    # print(inspect.getsource(decorated_func))  # def wrapper(*args, **kwargs): .... return return_value
    # print(decorated_func(url='https://google.com'))  # param will go to kwargs
    # print(decorated_func('https://google.com'))  # param will go to agrs
    print(webpage)

    print("--------------")
    webpage = fetch_webpage('https://google.com')  # is wrapped with syntax sugar @ decorator
    print(webpage)

    print("--------------")
    actual_decorator = benchmark_with_param(iters=2)  # by fact actual_decorator function
    fetch_webpage_raw_new = actual_decorator(fetch_webpage_raw)  # by fact wrapper function
    webpage = fetch_webpage_raw_new('https://google.com')
    print(webpage)

    print("--------------")
    webpage = fetch_webpage_dec_params('https://google.com')
    print(webpage)
