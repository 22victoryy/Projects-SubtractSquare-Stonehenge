"""
...
"""
from cchopsticks import GameState
from cchopsticks import ChopsticksState


class Game:
    """
    ...
    """

    def __init__(self, is_p1_turn):
        self.is_p1_turn = is_p1_turn
        self.current_state = GameState(is_p1_turn)

    def __eq__(self, other):
        return type(self) == type(other)

    def __str__(self):
        raise NotImplementedError

    def get_instructions(self) -> str:
        """"
        Returns the instruction of the game.
        """
        raise NotImplementedError

    def is_over(self, current_state):
        """
        bool
        """
        raise NotImplementedError

    def is_winner(self, player):
        """
        bool
        """
        raise NotImplementedError

    def str_to_move(self, num):
        """
        strategy
        """
        raise NotImplementedError


class Chopsticks(Game):
    """
    SubtractSquare
    """

    def __init__(self, is_p1_turn):
        Game.__init__(self, is_p1_turn) # bool
        if is_p1_turn:
            self.current_state = ChopsticksState("p1", [1, 1, 1, 1])
        else:
            self.current_state = ChopsticksState("p2", [1, 1, 1, 1])

    def get_instructions(self) -> str:
        """"
        Returns the instruction of the game.
        """
        return "Each of two players begins with one finger pointed up on each" \
               "of their hands. 2. Player A touches one hand to one of " \
               "Player B's hands, increasing the number of fingers pointing up"\
               "on Player B's hand by the number on Player A's hand. The " \
               "number pointing up on Player A's hand remains the same. 3. " \
               "If Player B now has five fingers up, that hand becomes dead or"\
               "unplayable. If the number of fingers should exceed five, " \
               "subtract five from the sum. 4. Now Player B touches one " \
               "hand to one of Player A's hands, and the distribution of " \
               "fingers proceeds as above, including the possibility of a " \
               "dead hand. 5. Play repeats the above steps until some player " \
               "has two dead hands, thus losing."

    def is_over(self, current_state):
        """
        bool
        """
        if current_state.player1l == 0 and current_state.player1r == 0:
            return True
        elif current_state.player2l == 0 and current_state.player2r == 0:
            return True
        return False

    def is_winner(self, player: str):
        """
        bool
        """
        return self.is_over(self.current_state) \
            and self.current_state.current_player != player

    def str_to_move(self, move_to_make: str):
        """
        strategy
        """
        return move_to_make


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
