class Repr(type):
    """Чтобы создать свой собственный метакласс в Python, нужно воспользоваться подклассом type,
    стандартным метаклассом в Python.
     классы – это объекты, создающие экземпляры. Классы сами являются экземплярами метаклассов.
     https://proglib.io/p/metaclafsses-in-python
     https://realpython.com/python-metaclasses

     ABCMeta  метакласс, позволяющий создавать абстрактные базовые классы
     """

    def stringify(cls):  # THIS IS WORKING ONLY AS AUDI CLASS METHOD
        return cls.__class__.__name__

    def __repr__(cls):  # THIS IS WORKING ONLY AS AUDI CLASS METHOD
        return cls.__name__


class MultiBases(Repr):
    def __new__(cls, clsname, bases, clsdict):
        if len(bases) > 2:
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
    # print(Audi.stringify())  # Attr100
    print(Audi)  # Audi

    # print(Audi().stringify()) # BECAUSE METACLASSES ARE ONLY FOR CLASSES AND NOT INSTANCES !
    # SO Repr class will not appear in mro
    print(Audi().attr)
    audi = Audi()
    print(audi)
    print(audi.__repr__())


    # Also we can construct classes on fly
    def init_constructor(self, arg):
        """lets create class in runtime
        constructor"""
        self.constructor_arg = arg


    class Sedan:
        pass


    # BMW = type("BMW", (Car, Attr100), {  # not the case cause mro gets not what i wanted
    BMW = type("BMW", (Sedan, Car), {  # I DONT KNOW HOW TO PASS METACLASS HERE
        # "__metaclass__": Attr100,  # seems like it have no effect
        # method
        "__init__": init_constructor,
        # data members
        "car_models": ["X1", "M3"]

    })
    print(BMW)
    print(BMW.mro())
    print(BMW("Test"))

    # print(dir(BMW))
    # print(help(BMW))
