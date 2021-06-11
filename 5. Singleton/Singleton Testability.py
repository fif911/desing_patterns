"""
Singleton design pattern
we will take a look at the problems with singleton and how they can be resolved

So in this example we show that:
test_dependent_total_population the dependent population test is a vastly superior test because it's not tied up
to the singleton in any way. So we've highlighted on of the weaknesses of a singleton
That if you take a direct dependency on it like in SingletonRecordFinder - than you are stacked with it
It should be possible to replace this dependency with something else (in our case the value whih is injected in the
init (Configurable record finder))
"""
import unittest


class Singleton(type):
    """ Singleton Metaclass implementation """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        """
        we want to load db only once
        """
        self.population = {}
        f = open('capitals.txt', 'r')
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i + 1].strip())
        f.close()


class SingletonRecordFinder:
    """
    High level module which uses the DB
    """

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]

        return result


class ConfigurableRecordFinder:
    """
    Use 2 types of DB to not to test on live production DB
    And with it we can make a dummy DB
    """

    def __init__(self, db=Database()):
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]

        return result


class DummyDatabase:
    """
    No way related to the real life db
    """
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name):
        return self.population[name]


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(17500000 + 17400000, tp)

    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(
            crf.total_population(['alpha', 'beta']),
            3
        )


if __name__ == '__main__':
    unittest.main()
