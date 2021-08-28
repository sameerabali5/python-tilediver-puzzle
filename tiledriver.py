# Name:         Sameera Balijepalli
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Spring 2021

# import random
from typing import List, Tuple
# from typing import Tuple


class PuzzleState:  # do not modify

    def __init__(self, tiles: Tuple[int, ...], path: str) -> None:
        self.tiles = tiles
        self.width = int(len(tiles) ** 0.5)
        self.path = path

    def __eq__(self, other: "PuzzleState") -> bool:
        return self.tiles == other.tiles and self.path == other.path

    def __repr__(self) -> str:
        return self.path


def check_letter(state: PuzzleState, move: str) -> PuzzleState:
    idx = state.tiles.index(0)
    dupe = state
    tlst = list(dupe.tiles)
    if move == "J": #down
        new = idx - dupe.width
        previousIdx = tlst[new]
        tlst[new] = 0
        tlst[new + dupe.width] = previousIdx
    if move == "K": #up
        new = idx + dupe.width
        previousIdx = tlst[new]
        tlst[new] = 0
        tlst[new - dupe.width] = previousIdx
    if move == "L": #right
        new = idx - 1
        previousIdx = tlst[new]
        tlst[new] = 0
        tlst[new + 1] = previousIdx
    if move == "H": #left
        new = idx + 1
        previousIdx = tlst[new]
        tlst[new] = 0
        tlst[new - 1] = previousIdx
    path = tuple(tlst)
    return PuzzleState(path, dupe.path + move)


def check_empty3(state: PuzzleState) -> List[PuzzleState]:
    array = []
    index = state.tiles.index(0)
    left, right = False, False
    up, down = False, False
    if state.width == 3:
        if index == 0 or index == 1 or index == 3\
        or index == 6 or index == 7:
            left = True
        if index == 0 or index == 1 or index == 2 or index == 3\
        or index == 5:
            up = True
        if index == 1 or index == 2 or index == 7\
        or index == 5 or index == 8:
            right = True
        if index == 3 or index == 5 or index == 6\
        or index == 7 or index == 8:
            down = True
    if left == True:
        array.append(check_letter(state, "H"))
    if down == True:
        array.append(check_letter(state, "J"))
    if up == True:
        array.append(check_letter(state, "K"))
    if right == True:
        array.append(check_letter(state, "L"))
    if index == 4:
        array.append(check_letter(state, "H"))
        array.append(check_letter(state, "J"))
        array.append(check_letter(state, "K"))
        array.append(check_letter(state, "L"))
    return array


def check_empty2(state: PuzzleState) -> List[PuzzleState]:
    array = []
    index = state.tiles.index(0)
    left, right = False, False
    up, down = False, False
    if state.width == 2:
        if index == 0 or index == 2:
            left = True
        if index == 1 or index == 3:
            right = True
        if index == 0 or index == 1:
            up = True
        if index == 2 or index == 3:
            down = True
    if left == True:
        array.append(check_letter(state, "H"))
    if down == True:
        array.append(check_letter(state, "J"))
    if up == True:
        array.append(check_letter(state, "K"))
    if right == True:
        array.append(check_letter(state, "L"))
    return array


def check_opposing(path: str, checker: str) -> bool:
    if path == "H" and checker == "L":
        return True
    if path == "J" and checker == "K":
        return True
    if path == "L" and checker == "H":
        return True
    if path == "K" and checker == "J":
        return True
    return False


def make_adjacent(state: PuzzleState) -> List[PuzzleState]:
    """
    Return a list of PuzzleState objects that represent valid, non-opposing
    moves from the given PuzzleState. A move is considered valid if it moves a
    tile adjacent to the blank tile into the blank tile. A move is considered
    non-opposing if it does not undo the previous move.

    >>> state = PuzzleState((3, 2, 1, 0), "")
    >>> make_adjacent(state)
    [PuzzleState((3, 0, 1, 2), "J"), PuzzleState((3, 2, 0, 1), "L")]
    """
    if state.width == 2:
        puzzle = check_empty2(state)
    else:
        puzzle = check_empty3(state)
    value = state.path
    if value != "":
        checker = value[-1]
        for i in puzzle:
            temp = str(i)
            temp = temp[-1]
            if check_opposing(temp, checker):
                puzzle.remove(i)
    return puzzle


def merge_sort(tiles: Tuple[int, ...]) -> int:
    """Returns inversion count using Merge Sort"""
    tileslst = list(tiles)
    tileslst.remove(0)
    tiles = tuple(tileslst)
    invCount = 0
    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                invCount += 1
    return invCount



def is_solvable(tiles: Tuple[int, ...]) -> bool:
    """
    Return a Boolean indicating whether the given tuple represents a solvable
    puzzle. Use the Merge Sort algorithm (possibly in a helper function) to
    efficiently count the number of inversions.

    >>> is_solvable((3, 2, 1, 0))
    True
    >>> is_solvable((0, 2, 1, 3))
    False
    """
    #width is odd number
    puzzle = PuzzleState(tiles, None)
    if puzzle.width % 2 != 0:
        if merge_sort(tiles) % 2 == 0:
            return True
    elif puzzle.width % 2 == 0:
        #even row
        if tiles[0] == 0 or tiles[1] == 0:
            if merge_sort(tiles) % 2 == 0:
                return True
        #odd row
        if tiles[2] == 0 or tiles[3] == 0:
            if merge_sort(tiles) % 2 != 0:
                return True
    return False


def shortest_path(check: List[PuzzleState]) -> PuzzleState:
    least = check[0]
    for i in check:
        if len(i.path) < len(least.path):
            least = i
    return least


def solve_puzzle(tiles: Tuple[int, ...]) -> str:
    """
    Return a string (containing characters "H", "J", "K", "L")
    representing the optimal number of moves to solve the given
    puzzle using Uniform Cost Search.
    A state is considered a solution if its tiles are sorted.

    >>> solve_puzzle((3, 2, 1, 0))
    "JLKHJL"
    """
    result = tuple(sorted(tiles))
    state = PuzzleState(tiles, "")
    check = make_adjacent(state)
    checker = check
    while check != None:
        least = shortest_path(checker)
        if result == least.tiles:
            return least.path
        else:
            checker.extend(make_adjacent(least))
            checker.remove(least)
    return "this puzzle is impossible to solve"


# def main() -> None:
#     random.seed(int(input("Random Seed: ")))
#     tiles = list(range(int(input("Puzzle Width: ")) ** 2))  # use 2 or 3
#     random.shuffle(tiles)
#     print("Tiles:", "[", " ".join(str(t) for t in tiles), "]")
#     if not is_solvable(tuple(tiles)):
#         print("Unsolvable")
#     else:
#         print("Solution:", solve_puzzle(tuple(tiles)))


if __name__ == "__main__":
    main()
