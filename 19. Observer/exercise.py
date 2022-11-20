import unittest


class Event(list):
    """List of functions you can call in sequence"""

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.rat_enters = Event()
        self.rat_dyes = Event()
        self.rat_notify = Event()


class Rat:
    def __init__(self, game: Game):
        self.attack = 1
        self.game = game

        self.game.rat_enters.append(self.rat_enters)
        self.game.rat_dyes.append(self.rat_dyes)
        self.game.rat_notify.append(self.rat_notify_from_others_that_they_exist)

        self.game.rat_enters(self)  # Call list of all rats subscribed

    def rat_enters(self, rat_that_just_entered):
        # print("Rat that just have entered")
        if self != rat_that_just_entered:
            self.attack += 1
            self.game.rat_notify(rat_that_just_entered)  # notify all other rats that one was added

    def rat_dyes(self, rat_=None):
        print(f"Rat that died {rat_}")
        self.attack -= 1

    def rat_notify_from_others_that_they_exist(self, new_rat):
        print("Notification recieved")
        if self == new_rat:
            self.attack += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.rat_dyes(self)

        self.game.rat_dyes.remove(self.rat_dyes)
        self.game.rat_notify.remove(self.rat_notify_from_others_that_they_exist)
        self.game.rat_enters.remove(self.rat_enters)
        return self


if __name__ == '__main__':
    game = Game()

    rat = Rat(game)
    print(f"Rat attack {rat.attack}, expected 1")

    rat2 = Rat(game)
    print(f"Rat1 attack {rat.attack}, expected 2")
    print(f"Rat2 attack {rat2.attack}, expected 2")

    with Rat(game) as rat3:
        print(f"Rat1 attack {rat.attack}, expected 3")
        print(f"Rat2 attack {rat2.attack}, expected 3")
        print(f"Rat3 attack {rat3.attack}, expected 3")

    print(f"Rat1 attack {rat.attack}, expected 2")
    print(f"Rat2 attack {rat2.attack}, expected 2")

#
# class TestCase(unittest.TestCase):
#
#     def test_three_rats_one_dies(self):
#         game = Game()
#
#         rat = Rat(game)
#         self.assertEqual(1, rat.attack)
#
#         rat2 = Rat(game)
#         self.assertEqual(2, rat.attack)
#         self.assertEqual(2, rat2.attack)
#
#         with Rat(game) as rat3:
#             self.assertEqual(3, rat.attack)
#             self.assertEqual(3, rat2.attack)
#             self.assertEqual(3, rat3.attack)
#
#         self.assertEqual(2, rat.attack)
#         self.assertEqual(2, rat2.attack)


# class Evaluate(unittest.TestCase):
#     def test_single_rat(self):
#         game = Game()
#         rat = Rat(game)
#         self.assertEqual(1, rat.attack)
#
#     def test_two_rats(self):
#         game = Game()
#         rat = Rat(game)
#         rat2 = Rat(game)
#         self.assertEqual(2, rat.attack)
#         self.assertEqual(2, rat2.attack)
#
#     def test_three_rats_one_dies(self):
#         game = Game()
#
#         rat = Rat(game)
#         self.assertEqual(1, rat.attack)
#
#         rat2 = Rat(game)
#         self.assertEqual(2, rat.attack)
#         self.assertEqual(2, rat2.attack)
#
#         with Rat(game) as rat3:
#             self.assertEqual(3, rat.attack)
#             self.assertEqual(3, rat2.attack)
#             self.assertEqual(3, rat3.attack)
#
#         self.assertEqual(2, rat.attack)
#         self.assertEqual(2, rat2.attack)
