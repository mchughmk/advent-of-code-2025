import pytest
from day4.day4 import PaperDiagram


class TestPaperDiagram:
    @pytest.mark.parametrize("row,column", [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)])
    def test_count_adjacent_rolls__when_none__expect_0(self, row, column):
        diagram = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        expected = 0
        paper_diagram = PaperDiagram(diagram)

        actual = paper_diagram.count_adjacent_rolls(row, column)

        assert expected == actual

    @pytest.mark.parametrize("row,column,expected", [(1, 1, 2), (1, 2, 2), (1, 3, 2), (2, 1, 2), (2, 2, 4), (2, 3, 2), (3, 1, 2), (3, 2, 2), (3, 3, 2)])
    def test_count_adjacent_rolls__when_rolls_exist__expect_expected(self, row, column, expected):
        diagram = [[".", "@", "."],
                   ["@", ".", "@"],
                   [".", "@", "."]]
        paper_diagram = PaperDiagram(diagram)

        actual = paper_diagram.count_adjacent_rolls(row, column)

        assert expected == actual

    def test_count_accessible_rolls__when_small_grid__expect_4(self):
        diagram = [[".", "@", "."],
                   ["@", ".", "@"],
                   [".", "@", "."]]
        expected = 4
        paper_diagram = PaperDiagram(diagram)

        actual = paper_diagram.count_accessible_rolls()

        assert expected == actual

    def test_find_accessible_rolls__when_small_grid(self):
        diagram = [[".", "@", "."],
                   ["@", ".", "@"],
                   [".", "@", "."]]
        expected = [(0, 1), (1, 0), (1, 2), (2, 1)]
        paper_diagram = PaperDiagram(diagram)

        actual = paper_diagram.find_accessible_rolls()

        assert expected == actual

    def test_count_accessible_rolls__when_sample_input__expect_13(self):
        input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
        diagram = [[col for col in row] for row in input.split()]
        expected = 13
        paper_diagram = PaperDiagram(diagram)

        actual = paper_diagram.count_accessible_rolls()

        assert expected == actual

    def test_remove_all_accessible_rolls__when_small_grid__expect_4(self):
        diagram = [[".", "@", "."],
                   ["@", ".", "@"],
                   [".", "@", "."]]
        expected = 4
        paper_diagram = PaperDiagram(diagram)
        paper_diagram.remove_all_accessible_rolls()

        actual = paper_diagram.removed_rolls

        assert expected == actual

    def test_remove_all_accessible_rolls__when_sample_input__expect_43(self):
        input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
        diagram = [[col for col in row] for row in input.split()]
        expected = 43
        paper_diagram = PaperDiagram(diagram)
        paper_diagram.remove_all_accessible_rolls()

        actual = paper_diagram.removed_rolls

        assert expected == actual
