"""
Implementation of a decorator in python is very specific
Functional decorator

Decorators are very useful to perform something around the function
"""
import time


# lets imagine we want to measure time taken to perform some_op()
# we can write a functional wrapper that takes some_op as a parameter and then uses it to perform time measurements

def time_it(func):
    # We define a new function which takes a function
    # and what it does: it build a new function, which is a wrapper of the original
    def wrapper():
        start = time.time()  # get current time
        result = func()  # call the function
        end = time.time()
        print(f'{func.__name__} took {int((end - start) * 1000)} ms')  # print some diagnostic info
        return result  # return the result of invocation

    # so basically here: time_it its function that returns a function
    # SOOOO
    # time_it get whatever function you give it.
    # Builds the wrapper around it
    # and return the newly created wrapper. BOOM
    return wrapper


@time_it
def some_op():
    print("Starting op")
    time.sleep(1)
    print("We are done")
    return 123


if __name__ == '__main__':
    # some_op()
    #
    # new_function = time_it(some_op)
    # new_function()
    # Obviously the same as
    # time_it(some_op)()
    #
    # So in python you have special syntax to apply this entire wrapper to the function everytime its get called
    # its done by using python's functional decorator:
    # @name_of_the_wrapper
    some_op()
