from typing import Any
from subtract_square import Game
from random import choice

# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Game) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def random_strategy(game: Game):
    """
    Random Strategy
    """
    a = game.current_state.get_possible_moves()
    return choice(a)





