"""The idea is:
whenever we operate on objects, we separate all of the invocations(вызов) into two different concepts
which are called
Query and Command

so Command is something that you send when you're asking for an action change (please set attack value to 2)

Query is asking for information (without necessarily changing it). please give me your attack value


And so we have something like CQS - having separate means of sending commands and queries
So instead of directly accessing a fields of a particular class, what you do is you send it a message, telling to please
give me a the contents of the field or you send a command that states please set the field to this particular value

And thanks to CoR you can also have other listeners to this command being sent and they can override the behaviour
of the actual command or indeed(в самом деле) the query
"""
