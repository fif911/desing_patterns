class Repr(type):
    """Чтобы создать свой собственный метакласс в Python, нужно воспользоваться подклассом type,
    стандартным метаклассом в Python.
     классы – это объекты, создающие экземпляры. Классы сами являются экземплярами метаклассов.
     https://proglib.io/p/metaclafsses-in-python
     https://realpython.com/python-metaclasses
     """

    def stringify(cls):  # THIS IS WORKING ONLY AS AUDI CLASS METHOD
        return cls.__class__.__name__

    def __repr__(cls):  # THIS IS WORKING ONLY AS AUDI CLASS METHOD
        return cls.__name__


class MultiBases(Repr):
    def __new__(cls, clsname, bases, clsdict):
        if len(bases) > 1:
            raise TypeError("Inherited multiple base classes!!!")
        return super().__new__(cls, clsname, bases, clsdict)


class Attr100(MultiBases):
    def __new__(cls, name, bases, dct):
        print(cls)  # <class '__main__.Attr100'>
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x


class OnlyAttr100(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x


# class Car(metaclass=StrNice):
# class Car(metaclass=Meta):
class Car(metaclass=MultiBases):
    pass


# class Audi(Car, metaclass=OnlyAttr100): # will not work TypeError: metaclass conflict
class Audi(Car, metaclass=Attr100):
    def __repr__(self):  # THIS IS WORKING ONLY AS AUDI() INSTANCE METHOD
        return self.__class__.__name__

    pass


if __name__ == '__main__':
    print(Audi.mro())  # [Audi, Car, <class 'object'>]
    print(Audi.stringify())  # Attr100
    # print(Audi().stringify()) # BECAUSE METACLASSES ARE ONLY FOR CLASSES AND NOT INSTANCES !
    print(Audi().attr)
    audi = Audi()
    print(audi)
    print(audi.__repr__())
    # SO Type class will not appear in mro
    # Also we can construct classes on fly
