"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any, Union, List
from copy import deepcopy


class Tree:
    """
    Tree ADT that holds the score of the given state and the childrne and move
    made to get to the said state
    """
    children: list
    state: object
    score: int
    id: int
    move: Any

    def __init__(self, id: int, move: Any = None,
                 state: Any = None,
                 children: List[Union['Tree', None]] = None):
        """
        Tree ADT

        """
        self.state = state
        self.children = children[:] if children is not None else []
        self.score = 0
        self.id = id
        self.move = move

    def __repr__(self):
        """
        Return string representation of Tree object
        """
        return "ID: {}, State: {}, Children: {}, Score: {}".format(
            self.id, self.state, self.children, self.score)


def get_move_score(game: Any, move: Any, starting_player: str) -> int:
    """ Return score of move on the state depending on the starting player
    """
    new_game = deepcopy(game)
    prev_state = new_game.current_state
    current_player = prev_state.get_current_player_name()
    current_state = new_game.current_state.make_move(move)

    new_game.current_state = current_state
    new_moves = new_game.current_state.get_possible_moves()
    other_player = ''
    if current_player == "p1":
        other_player = "p2"
    elif current_player == "p2":
        other_player = "p1"
    if new_game.current_state.get_possible_moves() == []:
        if new_game.is_winner(current_player):
            return new_game.current_state.WIN
        elif new_game.is_winner(other_player):
            return new_game.current_state.LOSE
        return new_game.current_state.DRAW

    return -1 * max([get_move_score(new_game, new_move, starting_player)
                     for new_move in new_moves])


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def minimax_recursive(game: Any) -> Any:
    """
    Minimax recursive
    """
    prev_state = game.current_state
    movelist = game.current_state.get_possible_moves()
    starting_player = game.current_state.get_current_player_name()
    if movelist == []:
        return 0
    scorelist = [get_move_score(game, move, starting_player)
                 for move in movelist]
    game.current_state = prev_state
    max_score = max(scorelist)
    return movelist[scorelist.index(max_score)]


def minimax_iterative(game: Any) -> Any:
    """
    Minimax iterative
    """
    new_list = []
    states = []
    new_list.append(Tree(1, None, game.current_state, None))
    prev_state = game.current_state
    i = 2
    while new_list != []:
        top_item = new_list.pop()
        if top_item.state.get_current_player_name() == 'p1':
            other_player = 'p2'
        else:
            other_player = "p1"
        game.current_state = top_item.state
        if top_item.state.get_possible_moves() == []:
            if game.is_winner(top_item.state.get_current_player_name()):
                top_item.score = top_item.state.LOSE
            elif game.is_winner(other_player):
                top_item.score = top_item.state.WIN
            else:
                top_item.score = top_item.state.DRAW
        elif top_item.children == [] or top_item.children is None:
            new_list.append(top_item)
            for move in top_item.state.get_possible_moves():
                new_state = top_item.state.make_move(move)
                new_item = Tree(i, move, new_state, None)
                new_list.append(new_item)
                top_item.children.append(new_item)
                i += 1
        elif top_item.children is not None:
            top_item.score = -1 * max([child.score for child in
                                       top_item.children])
            states.append(top_item)
    if states == []:
        return 0
    best_score = max([child.score for child in states[-1].children])
    get_index_best_state = [child.score for child in
                            states[-1].children].index(best_score)
    move_to_make = states[-1].children[get_index_best_state].move_made
    shortest_len = 100000000
    for item in states[-1].children:
        if item.score == best_score:
            if len(item.children) < shortest_len:
                shortest_len = len(item.children)
                move_to_make = item.move_made
    game.current_state = prev_state
    return move_to_make


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.
    """
    current_state = game.current_state
    best_move = None
    best_output = -2
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)
        score = new_state.rough_outcome() * -1
        if score > best_output:
            best_output = score
            best_move = move
    return best_move


#"a2_pyta.txt")
