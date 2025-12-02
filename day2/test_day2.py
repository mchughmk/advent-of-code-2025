from day2.day2 import find_invalid_ids_in_range, is_invalid, read_and_sum_invalid_ranges


def test_find_invalid_ids_in_range__when_11_22__expect_11_22():
    range_start = 11
    range_end = 22
    expected = [11, 22]

    actual = find_invalid_ids_in_range(range_start, range_end)

    assert expected == actual


def test_find_invalid_ids_in_range__when_95_115__expect_99_111():
    range_start = 95
    range_end = 115
    expected = [99, 111]

    actual = find_invalid_ids_in_range(range_start, range_end)

    assert expected == actual


def test_find_invalid_ids_in_range__when_998_1012__expect_999_1010():
    range_start = 998
    range_end = 1012
    expected = [999, 1010]

    actual = find_invalid_ids_in_range(range_start, range_end)

    assert expected == actual


def test_is_invalid__when_11__expect_true():
    test_val = "11"
    expected = True

    actual = is_invalid(test_val)

    assert expected == actual


def test_is_invalid__when_10__expect_false():
    test_val = "10"
    expected = False

    actual = is_invalid(test_val)

    assert expected == actual


def test_is_invalid__when_1010__expect_true():
    test_val = "1010"
    expected = True

    actual = is_invalid(test_val)

    assert expected == actual


def test_is_invalid__when_1188511885__expect_true():
    test_val = "1188511885"
    expected = True

    actual = is_invalid(test_val)

    assert expected == actual


def test_is_invalid__when_2121212118__expect_false():
    test_val = "2121212118"
    expected = False

    actual = is_invalid(test_val)

    assert expected == actual


def test_sample_expect_4174379265():
    range_str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    expected = 4174379265

    actual = read_and_sum_invalid_ranges(range_str)

    assert expected == actual
