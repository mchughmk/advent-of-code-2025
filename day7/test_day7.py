import pytest
from day7.day7 import *

sample_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


@pytest.mark.parametrize("row,expected", [(['S', '.', '.', '.'], 0), (['.', '.', 'S', '.'], 2), (['.', '.', '.', 'S'], 3)])
def test_find_start_index(row, expected):
    actual = find_start_index(row)

    assert expected == actual


def test_count_splits__when_sample_input__expect_21():
    diagram = [[x for x in line] for line in sample_input.split()]
    expected = 21

    actual = count_splits(diagram)

    assert expected == actual


def test_count_timelines__when_sample_input__expect_40():
    diagram = [[x for x in line] for line in sample_input.split()]
    expected = 40

    actual = count_timelines(diagram)

    assert expected == actual
