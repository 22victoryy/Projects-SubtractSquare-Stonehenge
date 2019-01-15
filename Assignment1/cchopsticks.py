"""
Generic game class
"""


class GameState:
    """
    Class state.
    """
    def __init__(self, current_player: str):
        self.current_player = current_player
        self.possible_moves = []

    def __eq__(self, other):
        return type(self) == type(other)

    def __str__(self):
        raise NotImplementedError

    def is_valid_move(self, num):
        """
        Returns the valid move.
        """
        raise NotImplementedError("No move has been made yet.")

    def get_possible_moves(self):
        """
        Gets the possible moves.
        """
        raise NotImplementedError("No moves available.")

    def make_move(self, move_to_make):
        """
        Makes the move.
        """
        raise NotImplementedError("Cannot make move due to no input.")

    def get_current_player_name(self):
        """
        ...
        """
        raise NotImplementedError("No such player is playing yet.")


class ChopsticksState(GameState):
    """
    Class for Chopsticks.
    """
    def __init__(self, is_p1_turn: str, l: list):
        GameState.__init__(self, is_p1_turn)
        self.player1l = l[0]
        self.player1r = l[1]
        self.player2l = l[2]
        self.player2r = l[3]

    def __eq__(self, other):
        pass

    def __str__(self):
        return "Player1: ({0} - {1}), Player2:({2} - {3})".format(
            self.player1l, self.player1r, self.player2l, self.player2r)

    def is_valid_move(self, move_to_make):
        """
        Gets the valid move.
        """
        return move_to_make in self.possible_moves

    def get_possible_moves(self):
        """
        Gets the possible moves available.
        """
        if self.current_player == "p1":
            if self.player1l != 0 and self.player2l != 0 and self.player2r != 0\
                    and self.player1r != 0:
                self.possible_moves = ["ll", "lr", "rl", "rr"]
            elif self.player1r == 0 and self.player1l != 0 and \
                    self.player2l != 0 and self.player2r != 0:
                self.possible_moves = ["ll", "lr"]
            elif self.player1r != 0 and self.player1l == 0 and \
                    self.player2l != 0 and self.player2r != 0:
                self.possible_moves = ["rl", "rr"]
            elif self.player1r != 0 and self.player1l != 0 and \
                    self.player2l != 0 and self.player2r == 0:
                self.possible_moves = ["rl", "ll"]
            elif self.player1r != 0 and self.player1l != 0 and \
                    self.player2l == 0 and self.player2r != 0:
                self.possible_moves = ["lr", "rr"]
            elif self.player1r == 0 and self.player1l != 0 and \
                    self.player2l != 0 and self.player2r != 0:
                self.possible_moves = ["lr"]
            elif self.player1r != 0 and self.player1l == 0 and \
                    self.player2l == 0 and self.player2r != 0:
                self.possible_moves = ["rr"]
            elif self.player1r == 0 and self.player1l != 0 and \
                    self.player2l != 0 and self.player2r == 0:
                self.possible_moves = ["ll"]
            elif self.player1r != 0 and self.player1l == 0 and \
                    self.player2l != 0 and self.player2r == 0:
                self.possible_moves = ["lr"]
            elif self.player1r == 0 and self.player1l == 0:
                self.possible_moves = []
        else:
            if self.player1l != 0 and self.player2l != 0 and self.player2r != 0\
                    and self.player1r != 0:
                self.possible_moves = ["ll", "lr", "rl", "rr"]
            elif self.player1l != 0 and self.player2l != 0 and \
                    self.player2r == 0 and self.player1r != 0:
                self.possible_moves = ["ll", "lr"]
            elif self.player1l != 0 and self.player2l == 0 and \
                    self.player2r != 0 and self.player1r != 0:
                self.possible_moves = ["rl", "rr"]
            elif self.player1l == 0 and self.player2l != 0 and \
                    self.player2r == 0 and self.player1r != 0:
                self.possible_moves = ["rl", "ll"]
            elif self.player1l != 0 and self.player2l != 0 and \
                    self.player2r == 0 and self.player1r == 0:
                self.possible_moves = ["lr", "rr"]
            elif self.player1l == 0 and self.player2l != 0 and \
                    self.player2r == 0 and self.player1r != 0:
                self.possible_moves = ["lr"]
            elif self.player1l == 0 and self.player2l == 0 and \
                    self.player2r != 0 and self.player1r != 0:
                self.possible_moves = ["rr"]
            elif self.player1l != 0 and self.player2l != 0 and \
                    self.player2r == 0 and self.player1r == 0:
                self.possible_moves = ["ll"]
            elif self.player1l != 0 and self.player2l == 0 and \
                    self.player2r != 0 and self.player1r == 0:
                self.possible_moves = ["rl"]
            elif self.player2r == 0 and self.player2l == 0:
                self.possible_moves = []
        return self.possible_moves

    def make_move(self, move_to_make):
        """
        As each player comes to their turn, the player makes the move.
        """
        new = ChopsticksState(self.current_player,
                              [self.player1l, self.player1r, self.player2l,
                               self.player2r])

        if self.current_player == "p1":
            if move_to_make == "rr":
                move = (self.player1r + self.player2r) % 5
                new.player2r = move
            elif move_to_make == "ll":
                move = (self.player1l + self.player2l) % 5
                new.player2l = move
            elif move_to_make == "rl":
                move = (self.player1r + self.player2l) % 5
                new.player2l = move
            elif move_to_make == "lr":
                move = (self.player1l + self.player2r) % 5
                new.player2r = move
            new.current_player = "p2"
        else:
            if move_to_make == "rr":
                move = (self.player1r + self.player2r) % 5
                new.player1r = move
            elif move_to_make == "ll":
                move = (self.player1l + self.player2l) % 5
                new.player1l = move
            elif move_to_make == "rl":
                move = (self.player2r + self.player1l) % 5
                new.player1l = move
            elif move_to_make == "lr":
                move = (self.player2l + self.player1r) % 5
                new.player1r = move
            new.current_player = "p1"
        return new

    def get_current_player_name(self):
        """
        Gets current player name.
        """
        return self.current_player


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
