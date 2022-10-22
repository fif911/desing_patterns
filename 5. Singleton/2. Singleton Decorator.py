"""
Store all unique instances in a class and retrieve when asked
"""


def singleton(class_):  # параметр декоратора это объэкт который мы обвернули в декоратор
    """
    We have a dict which takes care of whatever object wants to be a singleton. It's just going to store its instance
    and it's going to return that instance whenever somebody wants to

    This approach prevents the whole initialize or double invocation(вызов) thing
    """
    instances = {}  # list of unique class names

    def get_instance(*args, **kwargs):
        print("Get instance called")
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)  # init class with args and kwargs
        return instances[class_]  # save this class name to db

    return get_instance


# the same as Database = singleton(Database)

@singleton
class Database:

    def __init__(self, name):
        """Add the init to prove that it's not called twice"""

        self.name = name
        print('Loading the DB')

    def __str__(self):
        return f"DB: {self.name}"


if __name__ == '__main__':
    d1 = Database("MySQL")  # printed: Loading the DB
    print(d1)
    d2 = Database("Postgres")  # printed: nothing
    print(d1, "is the same as ", d2, "\n")
    print(d1 == d2)
