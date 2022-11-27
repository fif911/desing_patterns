from abc import ABC
from typing import List
from unittest import TestCase


class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures: List[Creature] = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index: int, c2_index: int):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        self.hit(c1, c2)
        self.hit(c2, c1)

        if (c1.health <= 0 and c2.health <= 0) or \
                (c1.health > 0 and c2.health > 0):  # both dead or both alive
            return -1
        else:
            return c1_index if c1.health > c1_index else c2_index

        # first_alive = c1.health > 0
        # second_alive = c2.health > 0
        # if first_alive == second_alive: return -1
        # return c1_index if first_alive else c2_index

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):

    def hit(self, attacker: Creature, defender: Creature):
        # print("TemporaryDamageCardGame HIT")
        # print(f"attacker attack {attacker.attack}. Defender health {defender.health}")
        if defender.health <= attacker.attack:  # Killed
            defender.health = 0


class PermanentDamageCardGame(CardGame):

    def hit(self, attacker, defender):
        defender.health -= attacker.attack


class Evaluate(TestCase):
    def test_impasse(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1), 'Combat should yield -1 since nobody died.')
        self.assertEqual(-1, game.combat(0, 1), 'Combat should yield -1 since nobody died.')

    def test_temporary_murder(self):
        c1 = Creature(1, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(1, game.combat(0, 1))

    def test_double_murder(self):
        c1 = Creature(2, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1))

    def test_permanent_damage_death(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 3)
        game = PermanentDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1), 'Nobody should win this battle.')
        self.assertEqual(1, c1.health)
        self.assertEqual(2, c2.health)
        self.assertEqual(1, game.combat(0, 1), 'Creature at index 1 should win this')
