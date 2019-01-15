"""
An implementation of Subtract Square.

NOTE: You do not have to run python-ta on this file.
"""
from game import Game
from subtract_square_state import SubtractSquareState


class SubtractSquareGame(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts):
        """
        Initialize this Game, using p1_starts to find who the first player is.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        num = int(input("Enter a number: "))
        self.current_state = SubtractSquareState(p1_starts, num)

    def get_instructions(self):
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        return "A non-negative whole number is chosen as the starting \n" \
               "valueby some neutral entity. In our case, a player will \n" \
               "choose it (i.e. through the use of input. The player whose \n" \
               "turn it is chooses some square of a positive whole number (\n" \
               "such as 1, 4, 9, 16, . . . ) to subtract from the \n" \
               "value, provided the chosen square is not larger. After \n" \
               "subtracting, we have a new value and the next player \n" \
               "chooses a square to ubtract from it. Play continues\n" \
               " to alternate between the two players until no moves are\n" \
               " possible. Whoever is about to play at that point loses!"

    def is_over(self, state):
        """
        Return whether or not this game is over.

        :return: True if the game is over, False otherwise.
        :rtype: bool
        """
        return state.current_total == 0

    def is_winner(self, player):
        """
        Return whether player has won the game.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string):
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.
        """
        if not string.strip().isdigit():
            return -1

        return int(string.strip())


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
