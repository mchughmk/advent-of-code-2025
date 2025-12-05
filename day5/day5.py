import pandas as pd
import piso

from os.path import dirname, join
from utils import read_input

piso.register_accessors()


class Inventory:
    def __init__(self, input: list):
        self.fresh_ingredients: pd.arrays.IntervalArray = []
        self.available_ingredients: list[int] = []

        self.parse_input(input)

    def parse_input(self, input: list[str]):
        fresh_ingredients = pd.arrays.IntervalArray.from_tuples(
            [x for x in input if isinstance(x, tuple)])
        self.fresh_ingredients = fresh_ingredients.piso.union()

        self.available_ingredients = [
            x for x in input if not isinstance(x, tuple)]

    def count_fresh_available_ingredients(self) -> int:
        count = 0
        for ingredient in self.available_ingredients:
            if any(self.fresh_ingredients.contains(ingredient)):
                count += 1

        return count

    def count_fresh_ingredient_ids(self) -> int:
        return sum([x.length for x in self.fresh_ingredients])

    def __str__(self):
        return f"Available fresh ingredients: {self.count_fresh_available_ingredients()}"


def parse_input_line(line: str):
    if not line:
        return "--"

    split_value = line.split("-")

    if len(split_value) == 2:
        return (int(split_value[0]) - 1, int(split_value[1]))
    else:
        return int(split_value[0])


def main():
    input = read_input(join(dirname(__file__), "input.txt"),
                       lambda line: parse_input_line(line))
    inventory = Inventory(input)

    print(inventory)


if __name__ == "__main__":
    main()
