# Strategy

*System behaviour partially specified at runtime*

### Definition

Strategy design pattern enables the exact behaviour of a system at a run-time.

So at run time you:

- Specify actual details
- Feed them to component that able to consume them
- And then this component uses high-level approach with your low-level strategy to actually do something

### Motivation

Many algorithms in a system can be decomposed into higher- and lower- level parts
where high-level algorithm can then be reused for serving some other purpose:

- E.g. For making tea and coffee you can have one general **'beverage-specific' strategy**

