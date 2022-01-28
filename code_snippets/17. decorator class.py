"""
Often, it is desirable to define a decorator as a class.
In python, any object can be a function if it implements the __call__ method.

There are a few notable differences between this class decorator and the function decorator:
- There is an inherent separation between methods executed at initialisation time (__init__),
and execution time (__call__)
- When the decorator is executed, the wrapped function is no longer passed as an argument, as this has already
happened at initialisation time.
So the wrapped function must be saved as a class attribute to be retrieved at execution time.
- Since execution happens separately to initialisation, we no longer need the inner wrapped function,
as when the decorator is executed, the wrapped function may also be executed

https://www.techblog.moebius.space/posts/2019-06-22-third-time-lucky-with-python-decorators/#2-decorator-classes
"""


def always_fail_raw():
    return False


class Retry:
    """This is class decorator"""

    def __init__(self, func):
        print("Decorator has initialised, with function %s" % func.__name__)
        self.func = func
        self.max_attempts = 3

    def __call__(self, *args, **kwargs):
        print("Called Retry decorator class")
        attempts = 0
        while attempts <= self.max_attempts:
            print("Running %s, attempt %s" % (self.func.__name__, attempts))
            function_result = self.func(*args, **kwargs)
            if function_result:
                return function_result
            attempts += 1


@Retry  # also it's possible to pass params into class but its a bit of a pain
def always_fail_raw_decorated(v1, v2):  # can be with params
    return False


if __name__ == '__main__':
    # Naively, this is how the class may be used without the decorator syntax:
    retry = Retry(always_fail_raw)
    retry()

    # And now with decorator syntax:
    always_fail_raw_decorated(1, 2)  # initialization happens before first line of code executed
    # and function is ready to be used
