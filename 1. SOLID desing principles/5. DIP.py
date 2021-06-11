"""
Dependency Inversion

High level classes classes and modules should not depend on low level modules, Instead they should depend on
abstractions.
We mean by abstraction the class with abstract methods. So you want to depend on interfaces rather than concrete
implementations

We did all these to avoid depending on internal implementations!
We introduced the interface RelationshipsBrowser
"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipsBrowser:
    """Interface for finding somebody's children
    we can delete it and it will still work cause of duck typing BUT it's a very friendly way to let people know that
    THIS IS HOW YOU IMPLEMENT a RelationshipsBrowser

    So for testing you can use some other class "fake browser" that will not go to real DB as Relationships may do
        fake browser will just return mocked data or some info from in memory storage
    """

    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipsBrowser):  # low level module - cause dealing with the storage
    """
    Store all the different relations.
    """

    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        """
        Why it's better.
        If you change the type of relations. You can rewrite this method. And the client will use
        the same function. (he not longer depend on concrete implementation)
        """
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# in order to brake DIP we will create high level module
class Research:  # high level module = basically uses other modules
    """Attempt to find all of the children of John

    And everything seems to work. But there is a huge problem
    The relations is the way relation module stores the relations at the moment it's a list. But if you will want
    To change it to a dict or some storage structure the code in init will break

    So if you have dependency on the storage implementation it's better to provide utility methods right in
    Relationships (low level module) to perform the search cause if ypu change the storage imlementation
    the whole search logic would be completely different

    How to fix it.
    First of all define the interface for low level module so research should not depend on concrete implementation
    which is Relationships. It should depend on on some sort of abstraction that can subsequently change. And you
    might change it for example for purposes of testing
    """

    # def __init__(self, relationships: Relationships):
    # In this case you accessing the internal storage mechanism of relationships which is LOW level module
    # in your HIGH level module. Which is a bad thing.

    # relations = relationships.relations
    # for r in relations:
    #     if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #         print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}.')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child2)
relationships.add_parent_and_child(parent, child1)

Research(relationships)
