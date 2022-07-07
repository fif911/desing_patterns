"""
Chain of Responsibility: A chain of components who all get a chance to process a command or a query,
optionally having default processing implementations and an ability to terminate(прекратить) the processing chain
Sequence of handlers processing an event one after another

Who should take the blame ?
Click a graphical element on a form:
 - button handles it, stops further processing
 - Underlying(Лежащий в основе) group box Maybe group box wants to handle an click ?
 - Underlying window

Collectible card game. You have a lot of creatures
- creature has attack and defence values
- Those can be boosted by other cards

"""
