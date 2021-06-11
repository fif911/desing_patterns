"""
Factory - component responsible solely(исключительно) for the wholesale (полный, оптовый, массовый)
(not piecewise creation of objects)
билдер как раз отвечает за построенеи объекта по частям

We need factories when our object creation logic becomes convoluted(запутаным)

We outsourcing the process of the creation of an object to a design pattern that you choose


IN modern naming - factory method is typically any method which creates an object.
By fact it's alternative to init that and have lots of advantages (good naming)

Wholesale(single statement that will create an object) object creation (non-piecewise, unlike Builder)
can be outsourced to:
- a separate method (Factory method ): typically static methods
- Move this whole idea to a separate class (Factory). So if you have class Food then you would have a Food Factory which
is in charge of manufacturing different types of objects
- Finally you can end up with hierarchy of factories corresponding to the hierarchy of your own types.
(Abstract factory design pattern)
"""