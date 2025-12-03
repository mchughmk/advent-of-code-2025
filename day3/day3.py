from os.path import dirname, join
from utils import read_input


def find_largest_joltage(bank: list[int]) -> int:
    largest = bank[:12]

    for battery in bank[12:]:
        for i, value in enumerate(largest):
            if i == 0:
                continue

            if value > largest[i-1]:
                largest = largest[:i-1] + largest[i:] + [battery]
                break

            if i == 11 and battery > value:
                largest = largest[:11] + [battery]

    return int("".join([str(x) for x in largest]))


def sum_largest_joltages(banks: list[list[int]]) -> int:
    return sum([find_largest_joltage(bank) for bank in banks])


def main():
    banks = read_input(join(dirname(__file__), "input.txt"),
                       lambda line: [int(x) for x in line])
    print(f"Sum: {sum_largest_joltages(banks)}")


if __name__ == "__main__":
    main()
