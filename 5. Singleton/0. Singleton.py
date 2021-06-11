"""
Singleton - Single instance - A component which is instantiated only once
Some components in the system makes sense to only init once

2 reasons: 1 - Init call is expensive. Something happens in initializer that you want to make only once
2 - or your object represents a resource and this res is only available in one instance
and you don't want to allow people to have more than 1 instance of such a resource + dont allow copying
+ we might also want to take care of lazy instantiation(реализация)
lazy instantiation - nobody gets to instantiate(создать экземпляр) the Singleton until
the Singleton is actually needed for something



Sometimes we
"""