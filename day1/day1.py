from os.path import dirname, join
from utils import read_input


def rotate_to_next_number(current_number: int, rotation: tuple[str, int] = ("R", 0)) -> int:
    next_number = current_number
    if (rotation[0] == "R"):
        next_number = current_number + rotation[1]
    else:
        next_number = 100 + current_number - rotation[1]

    return next_number % 100


def count_zero_intersects(current_number: int, rotation: tuple[str, int]) -> int:
    if rotation[0] == "R":
        return (current_number + rotation[1]) // 100

    return (rotation[1] // 100) + (1 if rotation[1] % 100 >= current_number and current_number != 0 else 0)


def count_zeroes(rotations: list[tuple[str, int]]) -> int:
    total_zeroes = 0
    current_number = 50
    for rotation in rotations:
        total_zeroes += count_zero_intersects(current_number, rotation)
        current_number = rotate_to_next_number(current_number, rotation)

    return total_zeroes


def main():
    rotations = read_input(
        join(dirname(__file__), "input.txt"), lambda line: (
            line[0], int(line[1:]))
    )
    print(f"Total Zeroes: {count_zeroes(rotations)}")


if __name__ == "__main__":
    main()
