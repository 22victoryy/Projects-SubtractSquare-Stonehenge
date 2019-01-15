#
"""
Game class for
"""
from current_state import State
from current_state import SubtractSquareState


class Game:
    """
    Generic game class
    """
    def __init__(self, is_p1_turn):
        self.is_p1_turn = is_p1_turn
        self.current_state = State(is_p1_turn)

    def __eq__(self, other):
        return type(self) == type(other) and self.is_p1_turn == other.is_p1_turn

    def __str__(self):
        raise NotImplementedError

    def get_instructions(self) -> str:
        """"
        Returns the instruction of the game.
        """
        raise NotImplementedError

    def is_over(self, current_state):
        """
        Checks if game is over.
        """
        raise NotImplementedError

    def is_winner(self, player):
        """
        Checks the winner of the game.
        """
        raise NotImplementedError

    def str_to_move(self, num):
        """
        Imports strategy.
        """
        raise NotImplementedError


class SubtractSquare(Game):
    """
    SubtractSquare
    """
    def __init__(self, is_p1_turn):
        self.is_p1_turn = is_p1_turn
        self.num = int(input('Enter a number: '))
        self.current_state = SubtractSquareState(is_p1_turn, self.num)

    def __eq__(self, other):
        pass

    def __str__(self):
        """
        """
        return "{}".format(self.num)

    def get_instructions(self) -> str:
        """"
        Returns the instruction of the game.
        >>> a = get_instrictons()
        >>> print(a)
        "A non-negative whole number is chosen as the starting \n" \
        "valueby some neutral entity. In our case, a player will \n" \
        "choose it (i.e. through the use of input. The player whose \n" \
        "turn it is chooses some square of a positive whole number (\n" \
        "such as 1, 4, 9, 16, . . . ) to subtract from the \n" \
        "value, provided the chosen square is not larger. After \n" \
        "subtracting, we have a new value and the next player \n" \
        "chooses a square to ubtract from it. Play continues\n" \
        " to alternate between the two players until no moves are\n" \
        " possible. Whoever is about to play at that point loses!"
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

    def is_over(self, current_state):
        """
        Checks if the game is over.
        """
        if current_state.num == 0:
            return True
        return False

    def is_winner(self, player):
        """
        Checks the winner of the game.
        """
        if self.is_over(self.current_state):
            return not self.current_state.get_current_player_name() == player
        return False

    def str_to_move(self, num):
        """
        Imports strategy.
        """
        return int(num)




if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
