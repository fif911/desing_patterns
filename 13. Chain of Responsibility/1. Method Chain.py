"""
Making multi player game with a lot creature roaming(бродить) the ground and attacking each other
and u deside u want to modify those creatures. E.g. creature picks up a sword and suddenly gets a boost to attack
lets see how we can model this scenario using the chain of responsibility design pattern
"""


class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


# imagine as creature walk around it gets modifications to its abilities

class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None  # store the next modifier in chain (you can have several modifiers)
        # next_modifier its a function pointer

    def add_modifier(self, modifier):
        # we need the ability to add a modifier to chain
        # if we already have a next element
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)  # we call add_modifier recursively
        else:
            self.next_modifier = modifier

    def handle(self):
        # location where this modifier gets applied by the creature
        # but of course it can only a single modifier in this large chain of responsibility
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        # key feature here. We need to call base class handle
        # cause base class here is the one that propagates the Chain of Responsibility
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name} defense")
            self.creature.defense += 1
        super().handle()


class NoBonusesModifier(CreatureModifier):
    """When u apply a modifier. NO other modifiers can be applied"""

    def handle(self):
        # not calling super().handle will broke the chain
        print("No bonuses for you.")


if __name__ == '__main__':
    goblin = Creature("Goblin", 1, 1)
    print(goblin)

    # for this CoR implementation you have a top level element
    root = CreatureModifier(goblin)

    # root.add_modifier(NoBonusesModifier(goblin)) # will break next modifiers

    root.add_modifier(IncreaseDefenseModifier(goblin))  # this will work
    # root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))  # this will not work
    # what to do if u want to disable all the bonuses

    root.handle()
    print(goblin)
