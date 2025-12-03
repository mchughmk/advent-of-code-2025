from day3.day3 import find_largest_joltage, sum_largest_joltages


def test_find_larget_joltage__when_987654321111111__expect_987654321111():
    bank = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]
    expected = 987654321111

    actual = find_largest_joltage(bank)

    assert expected == actual


def test_find_larget_joltage__when_811111111111119__expect_811111111119():
    bank = [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]
    expected = 811111111119

    actual = find_largest_joltage(bank)

    assert expected == actual


def test_find_larget_joltage__when_234234234234278__expect_434234234278():
    bank = [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8]
    expected = 434234234278

    actual = find_largest_joltage(bank)

    assert expected == actual


def test_find_larget_joltage__when_818181911112111__expect_888911112111():
    bank = [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1]
    expected = 888911112111

    actual = find_largest_joltage(bank)

    assert expected == actual


def test_sum_larget_joltages__when_sample_banks__expect_3121910778619():
    banks = [[9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1],
             [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
             [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8],
             [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1]]
    expected = 3121910778619

    actual = sum_largest_joltages(banks)

    assert expected == actual


def test_find_largest_joltage__first_input():
    bank = [int(x) for x in "3646122246265233144266436235253422621132626544356324544665325242262222212765227332424562134252555523"]
    expected = 776452555523

    actual = find_largest_joltage(bank)

    assert expected == actual
