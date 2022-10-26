"""
A mechanism for treating individual(scalar) objects and compositions of objects in a uniform manner

Goal of composite DP - to treat individual components and groups of objects in a uniform fashion

!!!! To provide identical interface over both aggregates(sets) of components and individual components !!!

Motivation:


https://stackify.com/oop-concepts-composition/
Composition is one of the fundamental concepts in object-oriented programming.
It describes a class that references one or more objects of other classes in instance variables.

Aggregation and Composition BUT THATS DIFFERENT
https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-aggregation-vs-composition/
Aggregation and Composition are subsets of association meaning they are specific cases of association.
In both aggregation and composition object of one class "owns" object of another class. But there is a subtle difference:
Aggregation implies a relationship where the child can exist independently of the parent.
Example: Class (parent) and Student (child). Delete the Class and the Students still exist.
Composition implies a relationship where the child cannot exist independent of the parent.
Example: House (parent) and Room (child). Rooms don't exist separate to a House.


1) Objects use other objects' properties/members through inheritance and composition (Состав)
2) Composition allows us make compound(составные, соединенные) objects
Example:
    You can have class person which is composed of name which is string but also Address which is its own object
    Mathematical expression composed of simple expressions
    A grouping of shapes that consist of several shapes
3) Composite DP is used to treat both singe (scalar) and composite objects uniformly
(in exactly same way)
Example:
    Foo and Sequence of Foo (yielding(производить) Foo) have common API

"""
