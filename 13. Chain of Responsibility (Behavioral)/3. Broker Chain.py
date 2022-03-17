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
    And we will use it in Broker implementation"""

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value  # value can be modified by modifiers in process
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Game:
    def __init__(self):
        self.queries = Event()  # This Event is something that anybody can subscribe to whenever somebody
        # sends a query
        # here is the idea:
        # somebody sends a query for a creature's attack val, but modifiers can listen to this event and they
        # can modify the returning value

    def perform_query(self, sender, query):
        self.queries(sender, query)  # invoke the event with sender and query


class CreatureModifier(ABC):
    def __init__(self, game, creature):
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


class Creature:
    def __init__(self, game, name, attack, defense):
        self.initial_defense = defense  # INITIAL value. Will be changed on fly
        self.initial_attack = attack  # INITIAL value. Will be changed on fly
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
        self.game.perform_query(self, q)  # sender is self; q is query
        return q.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


if __name__ == '__main__':
    game = Game()
    goblin = Creature(game, "Strong Goblin", 2, 2)  # creature in the game
    print(goblin)

    # dam = DoubleAttackModifier(game, goblin)  # as soon as it's build -> it's applied
    with DoubleAttackModifier(game, goblin):
        print(goblin)  # when we exit with we unsubscribe from query so we no longer modify the query
        # and therefore this modifier does not apply

    print(goblin)
    # you can add the different modifiers in a same fashion
    # And also what you can do. U can ensure that this modifiers have limited lifetime
    # you can use them with with key word
