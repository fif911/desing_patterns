"""
Flyweight - space optimization
Space optimization technique that lets us use less memory by storing externally the data associated with similar objects

https://refactoring.guru/ru/design-patterns/flyweight/python/example

- Avoid redundancy (избыточность,чрезмерность)
e.g. In massive multiple game
 - Plenty of users with identical first/last names
 - No sense in storing same first/last name over and over again
 - Store a list of names and references to them

e.g. text formatting in typical text editor (bold or italic text)
 - dont want each character to have a formatting character
 - operate on ranges (e.g.) line number, start/end positions
 intersections also should be supported (bold and italic at the same time )




"""
