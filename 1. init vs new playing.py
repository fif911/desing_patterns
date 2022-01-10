from datetime import date


class Boy:
    def __new__(cls, ):
        print(f"Boy __new__ {cls}")
        # return object.__new__(cls)
        # return super(Boy, cls).__new__(cls)  # if super(Student, cls).__new__(Gamer, *args, **kwargs)
        return super().__new__(cls)  # if super(Student, cls).__new__(Gamer, *args, **kwargs)
        # than   TypeError: super(type, obj): obj must be an instance or subtype of type


class Gamer:
    def __new__(cls, ):
        print(f"Gamer __new__ {cls}")
        # return object.__new__(cls)
        return super().__new__(cls)


class Student(Boy, Gamer):
    #  NOTE ! Class variable is  shared between all instances of the class.
    default_value = 0

    @staticmethod  # it's static method by default (in class "object")
    def __new__(cls, ):
        print(f"Student __new__ {cls}")
        # return super(Student, cls).__new__(Gamer, *args,
        #                                    **kwargs)  # AttributeError: 'Gamer' object has no attribute 'instance_method'
        # return super(Gamer,cls).__new__(Gamer, *args, **kwargs) # AttributeError: 'Gamer' object has no attribute 'instance_method'
        # return super(Gamer, cls).__new__(cls, *args,
        #                                    **kwargs)  # AttributeError: 'Gamer' object has no attribute 'instance_method'

        return super().__new__(cls)
        # return super().__new__(Boy)

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

    def __add__(self, other):
        return Person(self.name + other.name,
                      self.age + other.age)


if __name__ == '__main__':
    Student.instance_static_method()
    print(f'Student.default_value in Student now: {Student.default_value} ')
    Student.instance_class_method()

    studentObj = Student()
    if isinstance(studentObj, Boy) or isinstance(studentObj, Gamer):
        print(f"studentObj type is {type(studentObj)}")
        # exit(0)
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

    person1 = Person('person1 ', 21)
    person2 = Person.fromBirthYear('person2', 1996)  # class method. Factory for Person

    # print(person1.__secret_name()) # AttributeError: 'Person' object has no attribute '__secret_name'
    print(person1.age)
    print(person2.age)

    # print the result
    print(Person.isAdult(22))  # static method. Just like utility

    person3 = person1 + person2
    print(f"person3 = {person3}")
    print(person3.name)
    print(person3.age)
    person3
    # print(type(type(studentObj)))
