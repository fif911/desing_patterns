"""
You have a game and you want to have average statistics of all existing creatures

"""


class CreatureBadOne:
    def __init__(self):
        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    @property
    def sum_of_stats(self):
        return self.strength + self.agility + self.intelligence  # looks unstable (e.g. you could forget to add 1 stats)

    @property
    def max_stat(self):
        return max(self.strength, self.agility, self.intelligence)

    @property
    def average(self):
        return self.sum_of_stats / 3.0  # also unstable

    # how we can refactor this code ?


class CreatureBetter:
    """
    Approach called Ray-Backed Properties
    or in case of Python List-Backed Properties
    """
    # hidden class level properties
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10]  # store only one list of properties

    # we can expose separate attributes by using properties
    @property
    def strength(self):
        # return self.stats[0]  # is also a magic number, so we can make it more self-descriptive
        return self.stats[CreatureBetter._strength]

    @strength.setter  # implement descriptor protocol for attributes
    def strength(self, value):
        self.stats[CreatureBetter._strength] = value

    @property
    def agility(self):
        return self.stats[CreatureBetter._agility]

    @agility.setter
    def agility(self, value):
        self.stats[CreatureBetter._agility] = value

    @property
    def intelligence(self):
        return self.stats[CreatureBetter._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[CreatureBetter._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)  # Note how convenient

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average(self):
        return float(self.sum_of_stats) / len(self.stats)
