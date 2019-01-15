"""
Stonehenge Game
"""
from typing import Any
from game import Game
from stonehenge_state import StonehengeState


class StonehengeGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        self.p1_starts = p1_starts
        self.side_length = input('Enter a Number ')
        while not self.side_length.isdigit():
            self.side_length = input('Enter a Number: ')
        self.side_length = int(self.side_length)
        if self.side_length >= 6 or self.side_length < 1:
            raise Exception("Invalid Input!")
        self.current_state = StonehengeState(self.p1_starts, self.side_length)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        return 'Take turn claiming cells (The capital letters) ' \
                'when a player captures at least half of the cells ' \
                'in a ley line they capture the leyline and the ' \
                'player to capture at least half of all the ' \
                'leylines in game wins!'

    def is_over(self, state: 'StonehengeState') -> bool:
        """
        Return whether or not this game is over at state.

        """
        count_p2 = 0
        count_p1 = 0
        even_amount = len(state.ley_line_state) % 2 == 0
        for leyline in state.ley_line_state:
            if state.ley_line_state[leyline] == 1:
                count_p1 += 1
            elif state.ley_line_state[leyline] == 2:
                count_p2 += 1
        if (count_p1 >= len(state.ley_line_state) // 2 or
                count_p2 >= len(state.ley_line_state) // 2) and \
                even_amount:
            return True
        elif (count_p1 > len(state.ley_line_state) // 2 or
              count_p2 > len(state.ley_line_state) // 2) and \
                not even_amount:
            return True
        return False

    def is_winner(self, player: str) -> bool:
        """
        Returns which player won the game.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> Any:
        """
        Return the move in a form of a string.
        """
        move_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return string.strip() if string in move_list else -1


# if __name__ == "__main__":
#     from python_ta import check_all
#     check_all(config="a2_pyta.txt")
