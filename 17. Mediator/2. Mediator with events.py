from typing import Any, Union


class Event(list):
    """List of functions you can call in sequence"""

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    """Mediator
    Centrally available component

     Game generates events that players and coaches and viewers can subscribe to"""

    def __init__(self):
        self.events = Event()

    def fire(self, args):
        """Fire an event"""
        self.events(args)


class GoalScoredInfo:
    """Information Who scored a goals, how many goals scored overall"""

    def __init__(self, who_scored: str, goals_scored: int):
        self.who_scored = who_scored
        self.goals_scored = goals_scored


class Player:
    def __init__(self, name: str, game: Game):
        """Init person with name and set the Game(mediator) it should subscribe to """
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(args)


class Coach:
    """ Coach is a listener to events that game fires

    Subscribe to event to celebrate a goal,
    Also cheer the player who scored the goal, but only for the first 2 times"""

    def __init__(self, game):
        # append possible Coach actions that he could do based on what happens in the game
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args: Union[GoalScoredInfo, Any]):
        """Args is an GoalScoredInfo, so if the event is PlayerGotRedCard we don't want to celebrate a goal"""
        if isinstance(args, GoalScoredInfo) and \
                args.goals_scored <= 2:
            print(f"Coach say's: well done, {args.who_scored}!")


if __name__ == '__main__':
    game = Game()
    sam_player = Player("Sam", game)
    coach = Coach(game)

    sam_player.score()  # Coach will cheer
    sam_player.score()  # Coach will cheer
    sam_player.score()  # Coach won't cheer
