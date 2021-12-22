"""
Proxy - an interface for accessing a particular resource
Class that functions as an interface to a particular resource. That resource may be remote, expensive to construct,
or may require logging or some other added functionality



- u are calling foo.Bar()
This makes a lot of assumptions: e.g. foo is in the same process as Bar()
What if, later on, you want to put all Foo related operations into a separate process
So you will have 2 processes and u will share the vars between 2 them

So can u avoid changing already written code ?
Proxy to the rescue!

- Same interface, entirely different behaviour

    (This is a example of communication proxy but there are plenty:
    logging, virtual, guarding,...
"""
