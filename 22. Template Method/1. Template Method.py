"""Do boilerplate(шаблонний) code for a game"""
from abc import ABC, abstractmethod


class Game(ABC):
    """Skeleton for any game"""

    def __init__(self, number_of_players: int):
        self.number_of_players = number_of_players
        self.current_player = 0  # what inheritors can use

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()

        print(f"Player {self.winning_player} wins!")

    @abstractmethod
    def start(self): pass

    @property
    @abstractmethod
    def have_winner(self): pass

    @abstractmethod
    def take_turn(self): pass

    @property
    @abstractmethod
    def winning_player(self): pass


class Chess(Game):
    def __init__(self):
        super().__init__(2)  # number of players always 2
        self.max_turns = 10  # related to Chess only
        self.current_turn = 1  # related to Chess only

    def run(self):  # no need to override run (can be deleted)
        super().run()

    def start(self):
        print(f"Starting a game of chess with "
              f"{self.number_of_players} players")
        pass

    @property
    def have_winner(self):
        return self.current_turn == self.max_turns

    def take_turn(self):
        print(f"Turn {self.current_turn} taken by player {self.current_player}")
        self.current_turn += 1
        self.current_player = 1 - self.current_player  # Cycle between 1 and 0. Wow

    @property
    def winning_player(self):
        return self.current_player


if __name__ == '__main__':
    chess = Chess()
    chess.run()
