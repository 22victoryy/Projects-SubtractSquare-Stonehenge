# """
# ...
# """
#
#
# class State:
#     """
#     Class state.
#     """
#     def __init__(self, is_p1_turn):
#         self.is_p1_turn = is_p1_turn
#
#     def __eq__(self, other):
#         return type(self) == type(other) and \
#                self.is_p1_turn == other.is_p1_turn
#
#     def __str__(self):
#         if self.is_p1_turn is False:
#             if self.is_p1_turn is True:
#                 return "It is player 2's turn."
#             return "It is player 1's turn."
#         return "Game is Over"
#
#     def is_valid_move(self, counter):
#         """
#         ...
#         """
#         raise NotImplementedError("No move has been made yet.")
#
#     def get_possible_moves(self):
#         """
#         ...
#         """
#         raise NotImplementedError("No moves available.")
#
#     def make_move(self, move_to_make):
#         """
#         ...
#         """
#         raise NotImplementedError("Cannot make move due to no input.")
#
#     def get_current_player_name(self):
#         """
#         ...
#         """
#         raise NotImplementedError("No such player is playing yet.")
#
#
# class SubtractSquareState(State):
#     """
#     k
#     """
#     def __init__(self, is_p1_turn, num: int):
#         State.__init__(self, is_p1_turn)
#         self.num = num
#
#     def __eq__(self, other):
#         pass
#
#     def __str__(self):
#         t = str(self.num)
#         return "State value is " + t
#
#     def get_possible_moves(self):
#         """
#         Gets the possible moves.
#         >>> a = get_possible_moves()
#         >>> b = 4
#         >>> c = get_possible_moves(b)
#         >>> print(c)
#         [4]
#         """
#         newlist = []
#         if self.num == 1:
#             newlist.append(1)
#         for x in range(0, self.num):
#             if 0 < x ** 2 <= self.num:
#                 newlist.append(x ** 2)
#         return newlist
#
#     def is_valid_move(self, counter):
#         """
#         Checks if the move is valid.
#         >>> a = is_valid_move(self, 4)
#         >>> get_possible_moves = [4]
#         >>> print(a)
#         True
#         >>> b = is_valid_move(self, 5)
#         >>> print(b)
#         False
#         """
#         return counter in self.get_possible_moves()
#
#     def make_move(self, move_to_make):
#         """
#         Makes the next move.
#         >>> a = make_move()
#         >>> make_move(is_over(True))
#         >>> print(a)
#         "Player 1 made the move {}."
#         """
#         if self.get_current_player_name() == "p1":
#             new = SubtractSquareState(False, self.num)
#             new.num = self.num - move_to_make
#
#         else:
#             new = SubtractSquareState(True, self.num)
#             new.num = self.num - move_to_make
#         return new
#
#     def get_current_player_name(self):
#         """
#         Gets current player name.
#         >>> a = get_current_player_name()
#         >>> print(a)
#         "p2"
#         >>> b = self.is_p1_turn
#         >>> c = get_current_player_name(b)
#         >>> print(c)
#         >>> "p1"
#         """
#         if self.is_p1_turn:
#             return "p1"
#         return "p2"

"""
...
"""


class State:
    """
    Class state.
    """
    def __init__(self, is_p1_turn):
        self.is_p1_turn = is_p1_turn

    def __eq__(self, other):
        return type(self) == type(other) and \
               self.is_p1_turn == other.is_p1_turn

    def __str__(self):
        if self.is_p1_turn is False:
            if self.is_p1_turn is True:
                return "It is player 2's turn."
            return "It is player 1's turn."
        return "Game is Over"

    def is_valid_move(self, counter):
        """
        ...
        """
        raise NotImplementedError("No move has been made yet.")

    def get_possible_moves(self):
        """
        ...
        """
        raise NotImplementedError("No moves available.")

    def make_move(self, move_to_make):
        """
        ...
        """
        raise NotImplementedError("Cannot make move due to no input.")

    def get_current_player_name(self):
        """
        ...
        """
        raise NotImplementedError("No such player is playing yet.")


class SubtractSquareState(State):
    """
    k
    """
    def __init__(self, is_p1_turn, num: int):
        State.__init__(self, is_p1_turn)
        self.num = num

    def __eq__(self, other):
        pass

    def __str__(self):
        t = str(self.num)
        return "State value is " + t

    def get_possible_moves(self):
        """
        Gets the possible moves.
        >>> a = get_possible_moves()
        >>> b = 4
        >>> c = get_possible_moves(b)
        >>> print(c)
        [4]
        """
        newlist = []
        if self.num == 1:
            newlist.append(1)
        for x in range(0, self.num):
            if 0 < x ** 2 <= self.num:
                newlist.append(x ** 2)
        return newlist

    def is_valid_move(self, counter):
        """
        Checks if the move is valid.
        >>> a = is_valid_move(self, 4)
        >>> get_possible_moves = [4]
        >>> print(a)
        True
        >>> b = is_valid_move(self, 5)
        >>> print(b)
        False
        """
        return counter in self.get_possible_moves()

    def make_move(self, move_to_make):
        """
        Makes the next move.
        >>> a = make_move()
        >>> make_move(is_over(True))
        >>> print(a)
        "Player 1 made the move {}."
        """
        if self.get_current_player_name() == "p1":
            new = SubtractSquareState(False, self.num)
            new.num = self.num - move_to_make

        else:
            new = SubtractSquareState(True, self.num)
            new.num = self.num - move_to_make
        return new

    def get_current_player_name(self):
        """
        Gets current player name.
        >>> a = get_current_player_name()
        >>> print(a)
        "p2"
        >>> b = self.is_p1_turn
        >>> c = get_current_player_name(b)
        >>> print(c)
        >>> "p1"
        """
        if self.is_p1_turn:
            return "p1"
        return "p2"


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
