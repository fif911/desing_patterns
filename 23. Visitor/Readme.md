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

