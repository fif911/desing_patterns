# Template Method

*A high-level blueprint for an algorithm to be completed by inheritors*

### Definition

Allows us to define the 'skeleton' of the algorithm, with concrete implementations defined in subclasses

### Motivation

The system can be decomposed into multiple components. Ofter we have same generic algorithm but some different concrete
implementations needed.

In Template Method:

1) Overall algorithm is defined in base class with some abstract members.
2) Inheritors override the abstract members
3) And then template method is invoked to get work done

### Does the same thing as Strategy DP but via inheritance

(Whereas 'Strategy' DP pass class as parameter and then methods are called, is Template Method DP the same thing is
done via inheritance )