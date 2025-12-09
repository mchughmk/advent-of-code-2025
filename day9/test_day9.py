import pytest
from shapely import Point
from day9.day9 import *

sample_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

sample_points = [Point(*line.split(",")) for line in sample_input.split()]


def test_find_largest_rectangle__when_sample_input__expect_50():
    expected = 50

    actual = find_largest_rectangle(sample_points)

    assert expected == actual


def test_find_largest_green_rectangle__when_sample_input__expect_24():
    expected = 24

    actual = find_largest_green_rectangle(sample_points)

    assert expected == actual
