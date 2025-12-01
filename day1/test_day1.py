from day1.day1 import rotate_to_next_number, count_zeroes


def test_rotate_to_next_number__when_no_rotations__expect_current_number():
    expected = 0

    actual = rotate_to_next_number(0)

    assert expected == actual


def test_rotate_to_next_number__when_right_1__expect_current_number_plus_1():
    rotation = ("R", 1)
    expected = 1

    actual = rotate_to_next_number(0, rotation)

    assert expected == actual


def test_rotate_to_next_number__when_right_2__expect_current_number_plus_2():
    rotation = ("R", 1)
    expected = 1

    actual = rotate_to_next_number(0, rotation)

    assert expected == actual


def test_rotate_to_next_number__when_left_1__expect_current_number_minus_1():
    rotation = ("L", 1)
    expected = 9

    actual = rotate_to_next_number(10, rotation)

    assert expected == actual


def test_rotate_to_next_number__when_left_2__expect_current_number_minus_2():
    rotation = ("L", 2)
    expected = 8

    actual = rotate_to_next_number(10, rotation)

    assert expected == actual


def test_rotate_to_next_number__when_right_1_and_current_99__expect_0():
    rotation = ("R", 1)
    expected = 0

    actual = rotate_to_next_number(99, rotation)

    assert expected == actual


def test_rotate_to_next_number__when_right_2_and_current_99__expect_1():
    rotation = ("R", 2)
    expected = 1

    actual = rotate_to_next_number(99, rotation)

    assert expected == actual


def test_rotate_to_next_number__when_left_1_and_current_0__expect_99():
    rotation = ("L", 1)
    expected = 99

    actual = rotate_to_next_number(0, rotation)

    assert expected == actual


def test_rotate_to_next_number__when_left_2_and_current_0__expect_98():
    rotation = ("L", 2)
    expected = 98

    actual = rotate_to_next_number(0, rotation)

    assert expected == actual


def test_count_zeroes__when_no_rotations__expect_0():
    expected = 0

    actual = count_zeroes([])

    assert expected == actual


def test_count_zeroes__when_left_50__expect_1():
    rotations = [("L", 50)]
    expected = 1

    actual = count_zeroes(rotations)

    assert expected == actual


def test_count_zeroes__when_right_50__expect_1():
    rotations = [("R", 50)]
    expected = 1

    actual = count_zeroes(rotations)

    assert expected == actual


def test_count_zeroes__when_right_51_left_1__expect_1():
    rotations = [("R", 51), ("L", 1)]
    expected = 2

    actual = count_zeroes(rotations)

    assert expected == actual


def test_sample__expect_6():
    rotations = [("L", 68), ("L", 30), ("R", 48), ("L", 5), ("R", 60),
                 ("L", 55), ("L", 1), ("L", 99), ("R", 14), ("L", 82)]
    expected = 6

    actual = count_zeroes(rotations)

    assert expected == actual
