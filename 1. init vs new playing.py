from datetime import date


class Student:
    #  NOTE ! Class variable is  shared between all instances of the class.
    default_value = 0

    @staticmethod  # it's static method by default (in class "object")
    def __new__(cls):
        print("__new__")
        # super.__new__(cls) # TypeError: super.__new__(Student): Student is not a subtype of super Не получится
        return object.__new__(cls)

    def __init__(self):
        print("__init__")
        self.instance_method()

    def instance_method(self):
        self.default_value  # noqa
        print('instance_method success!')

    @staticmethod
    def instance_static_method():
        print('instance_static_method success!')

    @classmethod
    def instance_class_method(cls):
        cls.default_value = 1
        print('instance_class_method success!')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

    def __secret_name(self):
        return f"secret_name: {self.name} Toby Clark"


if __name__ == '__main__':
    Student.instance_static_method()
    print(f'Student.default_value in Student now: {Student.default_value} ')
    Student.instance_class_method()

    studentObj = Student()
    studentObj.instance_method()

    print(f'studentObj.default_value in studentObj now: {studentObj.default_value}')  # ВААААУУУ. Выведется 1
    print(f'Student.default_value in Student now: {Student.default_value}  \n')  # ВААААУУУ. Выведется 1

    """
    Т.е. : C помощью класс методов мы можем доставать и менять значения в классе. В статиках нет
    Так же что очень важно
     - We generally use class method to create factory methods. Factory methods return class objects
    ( similar to a constructor ) for different use cases.
     - We generally use static methods to create utility functions.
    """

    person1 = Person('mayank', 21)
    person2 = Person.fromBirthYear('mayank', 1996)  # class method. Factory for Person

    # print(person1.__secret_name()) # AttributeError: 'Person' object has no attribute '__secret_name'
    print(person1.age)
    print(person2.age)

    # print the result
    print(Person.isAdult(22))  # static method. Just like utility


    # print(type(type(studentObj)))
