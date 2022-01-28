"""
https://towardsdatascience.com/why-you-should-wrap-decorators-in-python-5ac3676835f9

The Problems of simple decorator
During a debugging process, we sometimes need to inspect particular objects to understand the implementation details
better. :
and problem - info will be returned about decorated func and not original one
print(say_hello) # <function invocation_log.<locals>.inner_func at 0x1115d6160>
help(say_hello)  Help on function inner_func in module __main__: it’s showing the information about the inner function
say_hello.__doc__  # will return Inner function within the invocation_log

In addition, sometimes we want to save our code using serializers, such as the pickle module in the standard library.
However, we can’t serialize the decorated function as its present form, because the module can’t serialize the
local object which is in the scope of the decorator function

print(pickle.dumps(say_hello)) # AttributeError: Can't pickle local object 'invocation_log.<locals>.inner_func'

The Solution
we can take advantage of the wraps function in the functools module in the standard library
wraps function is a decorator itself, and we’ll use this function to decorate the inner function by configuring
the to-be-decorated function
@wraps(func) # It’s just one line of code
 Let’s see how things are changed after this seemingly trivial change
"""
import inspect
import pickle
from functools import wraps


def invocation_log(func):
    @wraps(func)  # It’s just one line of code
    def inner_func(*args, **kwargs):
        """Inner function within the invocation_log"""
        print(f'Before Calling {func.__name__}')
        func(*args, **kwargs)
        print(f'After Calling {func.__name__}')

    return inner_func


@invocation_log
def say_hello(name):
    """Say hello to someone"""
    print(f"Hello, {name}!")


def check_decorator_wraps(decorated_func):
    print(decorated_func)
    help(decorated_func)
    print(decorated_func.__doc__)
    print(pickle.dumps(decorated_func))  # We’re now able to serialize the function for further processing.


if __name__ == '__main__':
    print(inspect.getsource(say_hello))  # @invocation_log def say_hello(name): ..
    say_hello("Alex")  # Its decorated function
    check_decorator_wraps(say_hello)
    say_hello_dump = pickle.dumps(say_hello)
    loaded_func = pickle.loads(say_hello_dump)
    print(loaded_func)  # <function say_hello at 0x0000016A32541670> # Its actually decorated function!
    loaded_func("Boba")
