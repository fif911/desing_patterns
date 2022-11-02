"""
Now what if we want to have attributes applied immediately without having to call handle and
without any kind of action (as soon as it's enters the game)

We will build Event broker (observer DP)
command query separation (command DP)
Whe idea is that you have different subsystems for processing commands i.e. things that ask u to do something
"""
from abc import ABC
from enum import Enum


class Event(list):
    """Event is list of functions that you can call
    And we will use it in Broker implementation

    Usage
    e = Event(func1,func2)
    e(..) # pass agrs that would be passed to functions

    It may be filled up with MODIFIERS and when we call query, it will get initial value
    and then subsequently transform it by applying modifiers
    """

    # def __call__(self, *args, **kwargs):
    def __call__(self, sender, query):
        # for item in self:
        for modifier_handle_function in self:
            modifier_handle_function(sender, query)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    """Perform query by event broker and on the way back apply modifiers"""

    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value  # value can be modified by modifiers in process
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class EventBroker:  # Game
    """Event broker"""

    def __init__(self):
        self.queries = Event()  # This Event is something that anybody can subscribe to whenever somebody
        # sends a query
        # here is the idea:
        # somebody sends a query for a creature's attack val, but modifiers can listen to this event and they
        # can modify the returning value

    def perform_query(self, sender, query: Query):
        # sender: Creature
        self.queries(sender, query)  # invoke the event with sender and query


class Creature:
    def __init__(self, game: EventBroker, name, initial_attack, initial_defense):
        self.initial_defense = initial_defense  # INITIAL value. Will be changed on fly
        self.initial_attack = initial_attack  # INITIAL value. Will be changed on fly
        self.name = name
        self.game = game  # Event Broker which takes care about our chain of responsibility

    # lets create a query mechanism for getting ACTUAL attack & defense values
    @property
    def attack(self):
        # query using event broker
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)  # sender is self; q is query
        return q.value

    @property
    def defense(self):
        # query using event broker
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        #  Send a request to an event broker to perform a query
        self.game.perform_query(self, q)  # sender is self; q is query.
        # value in query was transformed by modifiers in the list
        # that were subscribed to this creature's name
        # we get transformed value from query and return
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier(ABC):
    def __init__(self, game: EventBroker, creature: Creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)  # add function to list of functions

    def handle(self, sender, query: Query):
        # nothing to do in ABC modifier
        pass

    def __enter__(self):
        # just self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # you have to unsubscribe from the handler
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and \
                query.what_to_query == WhatToQuery.ATTACK:
            # than we can handle it
            query.value *= 2


if __name__ == '__main__':
    game = EventBroker()  # create event broker
    print(f"Game queries: {game.queries}")
    goblin = Creature(game, "Strong Goblin", 2, 2)  # creature in the game
    print(goblin)

    # dam = DoubleAttackModifier(game, goblin)  # as soon as it's build -> it's applied
    with DoubleAttackModifier(game, goblin):
        print(f"Game queries DoubleAttackModifier: {game.queries}")
        print(goblin)  # when we exit with we unsubscribe from query so we no longer modify the query
        # and therefore this modifier does not apply

    print(goblin)
    # you can add the different modifiers in a same fashion
    # And also what you can do. U can ensure that this modifiers have limited lifetime
    # you can use them with with key word
    print("After multiple context managers: ")
    with DoubleAttackModifier(game, goblin) and DoubleAttackModifier(game, goblin):
        print(game.queries)
        print(goblin)
    print(goblin)  # will not delete one modifier as they are same
