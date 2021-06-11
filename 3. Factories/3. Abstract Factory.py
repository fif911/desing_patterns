"""
Abstract factory - abstract based classes
The idea - if you have hierarchy of types, than you can have a corresponding hierarchy of factories
And at some point you would have an abstract factory as a base class of the other factories

Абстрактные классы широко фигурируют в ООП, часто всплывают в шаблонах проектирования. Они говорят, что общий
интерфейс уже обозначен, но этот класс еще не предназначен для использования, кроме как для наследования
от него конкретных потомков.
https://tirinox.ru/abstract-class-abc/
"""
from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink(ABC):
    # having abstract method here will though error  TypeError: Can't instantiate abstract class HotDrink
    # with abstract method consume
    # @abstractmethod # АБСТАКНЫЙ МЕТОД ОЗНАЧАЕТ ЧТО ЕГО НАДО ПЕРЕОПРЕДИЛИТЬ
    def consume(self):
        pass


class ABClassWithoutImplementingTheInterface(HotDrink):
    pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')


"""
Playing with ABC
HotDrink()  # can't be implemented if @abstractmethod added.
ABClassWithoutImplementingTheInterface()  # we still can create a ABC class without implementing non abstract
# method consume
Tea().consume()
"""


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


"""
Now we have hierarchy of different type. Base class - Drink and some inheritance

Imaging that preparation of tea or coffee are so so sophisticated(сложный) that you need a factory to prepare drink 
So in addition to hierarchy of different drinks we will have hierarchy of the factories 


"""


class HotDrinkFactory(ABC):
    """
    It's not need and can be commented. CAUSE PYTHON USES DUCK TYPING and in the factories list list is not typed as
    HotDrinkFactory. But it's good practise and mandatory in other strong typing languages to create base classes
    """

    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in teas bag, boil water. Pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


"""
Now we have types, we have hierarchy of types. So how to make a drinks
"""


def make_drink(type: str):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


# lets have a class, so organize things better by making separate component which will make use of the diff factories
# and stick them together. Also we will use our abstract class
class HotDrinkMachine:
    # there may have of making this but and this one of the ways
    # BUT this approach violates the OPC. cause when you will add new kind of drink you will have to go to this enum
    # and modify
    class AvailableDrink(Enum): # violates OCP
        COFFEE = auto()
        TEA = auto()

    factories = []  # list of all factories
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()  # name of the drink
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()  # calling any Factory with no arguments
                # eval from evaluate eval("2 ** 8") will return 256
                # https://proglib.io/p/dinamicheskoe-vypolnenie-vyrazheniy-v-python-funkciya-eval-2020-05-14
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available Drinks')
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0 - {len(self.factories) - 1})')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        # use the factory to make a drink
        # return eval the factory_name But as we already have the factory instance but we need to find it
        return self.factories[idx][1].prepare(amount)  # self.factories[idx] turple (factory_name, FactoryInstance)


if __name__ == '__main__':
    # entry = input('What kind of drink would you like?')
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()