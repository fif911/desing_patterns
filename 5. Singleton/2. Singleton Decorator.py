def singleton(class_):
    """
    We have a dict which takes care of whatever object wants to be a singleton. It's just going to store its instance
    and it's going to return that instance whenever somebody wants to

    This approach prevents the whole initialize or double invocation(вызов) thing
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:

    def __init__(self):
        """Add the init to prove that it's not called twice"""
        print('Loading the DB')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
