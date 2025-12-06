import re
from os.path import dirname, join
from utils import read_input


def get_vertical_problem(values: list[str]):
    numbers = ["".join([digit[index] for digit in values[:-1]]).strip()
               for index in range(len(values[0]))]
    return values[-1].strip().join(numbers[::-1])


def sum_problem_solutions(problems: list[str]) -> int:
    total = 0
    operators = get_operators(problems)

    index = 0
    for operator in operators:
        values = [row[index:index+len(operator)]
                  for row in problems[:-1]]
        problem = get_vertical_problem(values + [operator])
        total += eval(problem)
        index += len(operator) + 1

    return total


def get_operators(problems: list[str]) -> list[str]:
    operators_row = problems[-1]
    return re.split(r' (?=\S)', problems[-1])


def main():
    problems = read_input(join(dirname(__file__), "input.txt"))

    print(sum_problem_solutions(problems))


if __name__ == "__main__":
    main()
