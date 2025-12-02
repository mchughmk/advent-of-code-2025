import re
from os.path import dirname, join
from utils import read_input


def is_invalid(number: int, length: int = 1) -> bool:
    num_str = str(number)
    search_value = num_str[:length]
    search_times = len(num_str) // length

    if len(num_str) < 2:
        return False

    pattern = rf'({search_value}){{{search_times}}}'
    match = re.fullmatch(pattern, num_str)

    if match:
        return True

    if length + 1 > len(num_str) / 2:
        return False

    return is_invalid(number, length+1)


def find_invalid_ids_in_range(range_start: int, range_end: int) -> list[int]:
    invalid_ids = [int(x) for x in range(
        range_start, range_end + 1) if is_invalid(x)]

    return invalid_ids


def process_range(range: str) -> list[int, int]:
    return [int(x) for x in range.split("-")]


def process_input_line(line: str) -> list[list[int, int]]:
    return [process_range(range) for range in line.split(",")]


def sum_invalid_ranges(ranges: list[list[int, int]]) -> int:
    total = 0
    for range in ranges:
        total += sum(find_invalid_ids_in_range(range[0], range[1]))

    return total


def read_and_sum_invalid_ranges(range_str: str) -> int:
    ranges = process_input_line(range_str)
    return sum_invalid_ranges(ranges)


def main():
    ranges = read_input(join(dirname(__file__), "input.txt"))
    print(f"Sum: {read_and_sum_invalid_ranges(ranges[0])}")


if __name__ == "__main__":
    main()
