from functools import reduce

""""# LAMBDA 
structure of lambda:
    The keyword: lambda
    A bound variable: x
    A body: x
"""

# def identity(x): return x
# same as:
lambda x: x  # noqa

lambda x: x + 1  # noqa You can apply the function to an argument by surrounding the function and its argument
# with parentheses:
print((lambda x: x + 1)(2))  # 3
# (lambda x: x + 1)(2) == lambda 2: 2 + 1 ==  2 + 1 == 3
# Because a lambda function is an expression, it can be named
add_one = lambda x: x + 1
add_one(2)

#  Multi-argument functions expressed in Python lambdas:
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

(lambda x, y: x + y)(2, 3)  # such thing called  Immediately Invoked Function Expression
#  this format used to highlight the anonymous aspect of a lambda function

# Lambda functions are frequently used with higher-order functions, which take one or more functions as arguments
# or return one or more functions.
# A lambda function can be a higher-order function by taking a function (normal or lambda) as an argument
high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * x)  # 6
high_ord_func(2, lambda x: x + 3)  # 7
# new_function = lambda x: func(x, *secondary_args, **secondary_kwargs)

# Appropriate Uses of Lambda Expressions
# Classic Functional Constructs
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))  # ['CAT', 'DOG', 'COW']
list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))  # ['Cat', 'Dog', 'Cow']
# the easier approach would be  [x.capitalize() for x in ['cat', 'dog', 'cow']]
list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))  # ['dog', 'cow']
list(filter(lambda x: x % 2 == 0, range(11)))
#  the easier approach would be  [x for x in range(11) if x%2 == 0]

reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])  # 'cat | dog | cow'

# Key Functions
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids))  # Lexicographic sort
# ['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Integer sort
print(sorted_ids)  # ['id1', 'id2', 'id3', 'id22', 'id30', 'id100']

# PARTIAL FUNCTIONS
print("PARTIAL FUNCTIONS")
# Partial functions allow us to fix a certain number of arguments of a function and generate a new function
from functools import partial


# A normal function
def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x


# A normal function
def add(a, b, c):
    print(f"locals for add(a, b, c) = {locals()}")
    return 100 * a + 10 * b + c


# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 2, 3, 4)

# Calling g()
print(g(5))
# print(g()) # TypeError: f() missing 1 required positional argument: 'x'

# A partial function with b = 1 and c = 2
add_part = partial(add, c=2, b=1)
# Calling partial function
print(add_part(3))
KeyboardInterrupt