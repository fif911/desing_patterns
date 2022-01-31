"""
MRO method resolution order

With super we allow mro to decide the sequence in which we want to methods of parent classes

The Method Resolution Order (MRO) is the set of rules that construct the linearization.
In the Python literature, the idiom "the MRO of C" is also used as a synonymous for the linearization of the class C.

https://www.youtube.com/watch?v=zS0HyfN7Pm4&t=458s
"""


class Portishead:
    def __init__(self):
        print("Portishead")


class KanyeWest(Portishead):
    def __init__(self):
        print('Kanye West')
        # Portishead.__init__(self)
        super().__init__()
        # super(KanyeWest, self).__init__()  # Same as super().__init__()


class ASAPRocky(Portishead):
    def __init__(self):
        print('ASAP Rocky')
        # Portishead.__init__(self)
        super().__init__()


class ASAPSabbie(ASAPRocky, KanyeWest):
    def __init__(self):
        print('ASAP Sabbie')
        # ASAPRocky.__init__(self)
        # KanyeWest.__init__(self)
        # with calling strictly init of parent class we get: 
        # ASAP Sabbie
        # ASAP Rocky
        # Portishead
        # Kanye West
        # Portishead -> outputted twice. Thats not what we want usually
        # 
        # if we call super() -> MRO comes in. And it understand the diamond structure
        # so we will get
        super(ASAPSabbie, self).__init__()
        # ASAP Sabbie -> top
        # ASAP Rocky -> first inherited class
        # Kanye West -> second inherited class
        # Portishead -> bottom of the diamond


class Type(type):
    """Чтобы создать свой собственный метакласс в Python, нужно воспользоваться подклассом type,
    стандартным метаклассом в Python.
     классы – это объекты, создающие экземпляры. Классы сами являются экземплярами метаклассов.
     https://proglib.io/p/metaclafsses-in-python
     """

    def __repr__(cls):
        return cls.__name__


class O(object, metaclass=Type): pass
class A(O): pass
class B(O): pass
class C(O): pass
class D(O): pass
class E(O): pass
class K1(A, B, C): pass
class K2(D, B, E): pass
class K3(D, A): pass
class Z(K1, K2, K3): pass


if __name__ == '__main__':
    asap_sabbie = ASAPSabbie()
    print(f"list all methods and properties of class instance: {dir(asap_sabbie)}")
    print(ASAPSabbie.__mro__)

    print()
    print(Z.mro())
