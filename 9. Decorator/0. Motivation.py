"""
Adding behavior without altering the class itself

DECORATOR - Component that facilitates(способствовать) the addition of behaviors to individual objects
without inheriting from them

- Want to augment(увеличивать) an object with extra features
- Do not want to rewrite or alter existing code (Breaks OCP)
- Want to keep functionality separate
- Need to be able to interact with existing structures
Two options
 - use inheritance
 - But if for some reason is that what u dont want to do  - Build a Decorator, which simply references the
 decorated object(s)
"""
