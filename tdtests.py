# Name:         Sameera Balijepalli

import unittest

import tiledriver
from tiledriver import PuzzleState as PS
# only allowed use of from ... import

class TestCheckLetter(unittest.TestCase):
    def test_check_letter_1(self):
        state = PS((3, 2, 1, 0), "J")
        move = "J"
        self.assertEqual(tiledriver.check_letter(state, move),
        PS((3, 0, 1, 2), "JJ"))

    def test_check_letter_2(self):
        state = PS((0, 3, 1, 2), "J")
        move = "H"
        self.assertEqual(tiledriver.check_letter(state, move),
        PS((3, 0, 1, 2), "JH"))

    def test_check_letter_3(self):
        state = PS((3, 2, 1, 0), "L")
        move = "J"
        self.assertEqual(tiledriver.check_letter(state, move),
        PS((3, 0, 1, 2), "LJ"))

    def test_check_letter_4(self):
        state = PS((0, 3, 1, 2), "K")
        move = "H"
        self.assertEqual(tiledriver.check_letter(state, move),
        PS((3, 0, 1, 2), "KH"))

    def test_check_letter_5(self):
        state = PS((0, 3, 1, 2), "H")
        move = "K"
        self.assertEqual(tiledriver.check_letter(state, move),
        PS((1, 3, 0, 2), "HK"))

class TestCheckEmpty3(unittest.TestCase):
    def test_check_empty3_1(self):
        state = PS((3, 2, 1, 0, 6, 7, 9, 8, 5), "")
        # print("LOOK")
        self.assertEqual(tiledriver.check_empty3(state),
                         [PS((3, 2, 1, 6, 0, 7, 9, 8, 5),
                         "H"), PS((0, 2, 1, 3, 6, 7, 9, 8, 5),
                         "J"), PS((3, 2, 1, 9, 6, 7, 0, 8, 5),
                         "K")])

    def test_check_empty3_2(self):
        state = PS((3, 2, 1, 6, 7, 9, 0, 8, 5), "")
        self.assertEqual(tiledriver.check_empty3(state),
                         [PS((3, 2, 1, 6, 7, 9, 8, 0, 5),
                         "H"), PS((3, 2, 1, 0, 7, 9, 6, 8, 5),
                          "J")])

    def test_check_empty3_3(self):
        state = PS((3, 2, 0, 1, 6, 7, 9, 8, 5), "")
        self.assertEqual(tiledriver.check_empty3(state),
                         [PS((3, 2, 7, 1, 6, 0, 9, 8, 5),
                         "K"), PS((3, 0, 2, 1, 6, 7, 9, 8, 5),
                          "L")])

    def test_check_empty3_4(self):
        state = PS((0, 3, 2, 1, 6, 7, 9, 8, 5), "")
        self.assertEqual(tiledriver.check_empty3(state),
                         [PS((3, 0, 2, 1, 6, 7, 9, 8, 5),
                         "H"), PS((1, 3, 2, 0, 6, 7, 9, 8, 5),
                          "K")])

    def test_check_empty3_5(self):
        state = PS((3, 2, 1, 6, 7, 9, 8, 5, 0), "")
        self.assertEqual(tiledriver.check_empty3(state),
                         [PS((3, 2, 1, 6, 7, 0, 8, 5, 9),
                         "J"), PS((3, 2, 1, 6, 7, 9, 8, 0, 5),
                          "L")])


class TestCheckEmpty2(unittest.TestCase):
    def test_check_empty2_1(self):
        state = PS((3, 2, 1, 0), "")
        self.assertEqual(tiledriver.check_empty2(state),
                         [PS((3, 0, 1, 2), "J"),
                         PS((3, 2, 0, 1), "L")])

    def test_check_empty2_2(self):
        state = PS((0, 3, 1, 2), "")
        self.assertEqual(tiledriver.check_empty2(state),
                         [PS((3, 0, 1, 2), "H"),
                         PS((1, 3, 0, 2), "K")])

    def test_check_empty2_3(self):
        state = PS((3, 0, 1, 2), "")
        self.assertEqual(tiledriver.check_empty2(state),
                         [PS((3, 2, 1, 0), "K"),
                         PS((0, 3, 1, 2), "L")])

    def test_check_empty2_4(self):
        state = PS((3, 1, 0, 2), "")
        self.assertEqual(tiledriver.check_empty2(state),
                         [PS((3, 1, 2, 0), "H"),
                         PS((0, 1, 3, 2), "J")])

    def test_check_empty2_5(self):
        state = PS((4, 3, 2, 0), "")
        self.assertEqual(tiledriver.check_empty2(state),
                         [PS((4, 0, 2, 3), "J"),
                         PS((4, 3, 0, 2), "L")])

class TestCheckOpposing(unittest.TestCase):
    def test_check_opposing_1(self):
        self.assertTrue(tiledriver.check_opposing("H", "L"))

    def test_check_opposing_2(self):
        self.assertFalse(tiledriver.check_opposing("H", "J"))

    def test_check_opposing_3(self):
        self.assertTrue(tiledriver.check_opposing("J", "K"))

    def test_check_opposing_4(self):
        self.assertTrue(tiledriver.check_opposing("L", "H"))

    def test_check_opposing_5(self):
        self.assertFalse(tiledriver.check_opposing("H", "K"))


class TestMakeAdjacent(unittest.TestCase):

    def test_make_adjacent_1(self):
        state = PS((3, 2, 1, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 0, 1, 2), "J"),
                         PS((3, 2, 0, 1), "L")])

    def test_make_adjacent_2(self):
        state = PS((0, 3, 1, 2), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 0, 1, 2), "H"),
                         PS((1, 3, 0, 2), "K")])

    def test_make_adjacent_3(self):
        state = PS((3, 0, 1, 2), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 2, 1, 0), "K"),
                         PS((0, 3, 1, 2), "L")])

    def test_make_adjacent_4(self):
        state = PS((3, 1, 0, 2), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 1, 2, 0), "H"),
                         PS((0, 1, 3, 2), "J")])

    def test_make_adjacent_5(self):
        state = PS((4, 3, 2, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((4, 0, 2, 3), "J"),
                         PS((4, 3, 0, 2), "L")])


class TestMergeSort(unittest.TestCase):
    def test_merge_sort_1(self):
        self.assertEqual(tiledriver.merge_sort((3, 2, 1, 0)), 3)

    def test_merge_sort_2(self):
        self.assertEqual(tiledriver.merge_sort((0, 2, 1, 3)), 1)

    def test_merge_sort_3(self):
        self.assertEqual(tiledriver.merge_sort((1, 2, 3, 0)), 0)

    def test_merge_sort_4(self):
        self.assertEqual(tiledriver.merge_sort((0, 2, 1, 3,
        5, 7, 6, 9, 8)), 3)

    def test_merge_sort_5(self):
        self.assertEqual(tiledriver.merge_sort((0, 1, 3, 5,
        4, 6, 8, 7, 9)), 2)

class TestIsSolvable(unittest.TestCase):

    def test_is_solvable_1(self):
        self.assertTrue(tiledriver.is_solvable((3, 2, 1, 0)))

    def test_is_solvable_2(self):
        self.assertFalse(tiledriver.is_solvable((0, 2, 1, 3)))

    def test_is_solvable_3(self):
        self.assertFalse(tiledriver.is_solvable((1, 2, 3, 0)))

    def test_is_solvable_4(self):
        self.assertFalse(tiledriver.is_solvable((0, 2, 1, 3,
        5, 7, 6, 9, 8)))

    def test_is_solvable_5(self):
        self.assertTrue(tiledriver.is_solvable((0, 1, 3, 5,
        4, 6, 8, 7, 9)))

# class TestIsSorted(unittest.TestCase):
#     def test_is_sorted_1(self):
#         self.assertTrue(tiledriver.is_sorted((0, 1, 2, 3)))
#
#     def test_is_sorted_2(self):
#         self.assertFalse(tiledriver.is_sorted((1, 0, 2, 3)))
#
#     def test_is_sorted_3(self):
#         self.assertFalse(tiledriver.is_sorted((3, 2, 1, 0)))
#
#     def test_is_sorted_4(self):
#         self.assertFalse(tiledriver.is_sorted((1, 2, 3, 0)))
#
#     def test_is_sorted_5(self):
#         self.assertTrue(tiledriver.is_sorted((4, 5, 6, 7)))

class TestShortestPath(unittest.TestCase):
    def test_shortest_path_1(self):
        state = [PS((0, 3, 2, 1), "K")]
        self.assertEqual(tiledriver.shortest_path(state),
        PS((0, 3, 2, 1), "K"))

    def test_shortest_path_2(self):
        state = [PS((3, 2, 1, 0), "J")]
        self.assertEqual(tiledriver.shortest_path(state),
        PS((3, 2, 1, 0), "J"))

    def test_shortest_path_3(self):
        state = [PS((0, 3, 2, 1), "H")]
        self.assertEqual(tiledriver.shortest_path(state),
        PS((0, 3, 2, 1), "H"))

    def test_shortest_path_4(self):
        state = [PS((3, 0, 2, 1), "L")]
        self.assertEqual(tiledriver.shortest_path(state),
        PS((3, 0, 2, 1), "L"))

    def test_shortest_path_5(self):
        state = [PS((3, 0, 2, 1), "J")]
        self.assertEqual(tiledriver.shortest_path(state),
        PS((3, 0, 2, 1), "J"))


class TestSolvePuzzle(unittest.TestCase):

    def test_solve_puzzle_1(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 2, 1, 0)), "JLKHJL")

    def test_solve_puzzle_2(self):
        self.assertEqual(tiledriver.solve_puzzle((0, 1, 2, 3)),
        "HKLJHKLJHKLJ")

    def test_solve_puzzle_3(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 2, 0, 1)), "JHKLJ")

    def test_solve_puzzle_4(self):
        self.assertEqual(tiledriver.solve_puzzle((4, 3, 2, 0)), "JLKHJL")

    def test_solve_puzzle_5(self):
        self.assertEqual(tiledriver.solve_puzzle((5, 4, 3, 0)), "JLKHJL")



if __name__ == "__main__":
    unittest.main()
