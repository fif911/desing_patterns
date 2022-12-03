# Visitor

*Allows adding extra behaviours to entire hierarchies of classes*

### Definition

**A component (Visitor) that knows how to traverse a data structure composed of (possibly related) types.**

----

### Problem

We need to **define a new operation on the entire class hierarchy**, but obviously, **we don't want to modify every
class in hierarchy**.

Note:

* In all this hierarchy of classes **all objects are interrelated somehow** (e.g. paragraph might contain list of items)
* Also, these classes can be different, so we **need access to non-common aspects of classes in the hierarchy**.

### Solution

**Create an external component that somehow knows how to navigate the entire structure**.
(How to go to the paragraph and navigate to other elements in it).  
This component should ignore explicit type checks and make use of duck typing.  

- By using overloads your language starts to behave kind of like strongly typed languages
- Decorator for visitor can to be custom build one, but also a multipledispatch.dispatch
- By calling visit() we effectively traverse the whole structure

### Tech implementation

```python
# For best function overloads use
from multipledispatch import dispatch

class Visitor:
    
    @dispatch(Value)
    def visit(self, v):
        ...

    @dispatch(AdditionExpression)
    def visit(self, ae: AdditionExpression):
        ...
    
    @dispatch(MultiplicationExpression)
    def visit(self, me: MultiplicationExpression):
        ...
```