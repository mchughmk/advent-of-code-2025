from os.path import dirname, join
from utils import read_input


class PaperDiagram:
    def __init__(self, diagram) -> None:
        self.diagram = diagram
        self.removed_rolls = 0

    def _is_valid_spot(self, row, column) -> bool:
        return (row > 0 and row <= len(self.diagram)) and (column > 0 and column <= len(self.diagram[row-1]))

    def count_adjacent_rolls(self, row, column) -> int:
        adjacent = 0

        if self._is_valid_spot(row, column):
            for search_row in range(row - 1, row + 2):
                for search_col in range(column - 1, column + 2):
                    if not (row == search_row and column == search_col) and self._is_valid_spot(search_row, search_col) and self.diagram[search_row-1][search_col-1] == "@":
                        adjacent += 1

        return adjacent

    def count_accessible_rolls(self) -> int:
        if not self._is_valid_spot(1, 1):
            return 0

        accessible_spots = 0
        for row in range(1, len(self.diagram) + 1):
            for col in range(1, len(self.diagram[0]) + 1):
                if self.diagram[row-1][col-1] == "@" and self.count_adjacent_rolls(row, col) < 4:
                    accessible_spots += 1

        return accessible_spots

    def find_accessible_rolls(self) -> list[tuple[int, int]]:
        if not self._is_valid_spot(1, 1):
            return 0

        accessible_rolls = []
        for row in range(1, len(self.diagram) + 1):
            for col in range(1, len(self.diagram[0]) + 1):
                if self.diagram[row-1][col-1] == "@" and self.count_adjacent_rolls(row, col) < 4:
                    accessible_rolls += [(row-1, col-1)]

        return accessible_rolls

    def remove_all_accessible_rolls(self):
        accessible_rolls = self.find_accessible_rolls()
        while len(accessible_rolls) > 0:
            for roll in accessible_rolls:
                self.diagram[roll[0]][roll[1]] = "."
            self.removed_rolls += len(accessible_rolls)
            accessible_rolls = self.find_accessible_rolls()

    def __str__(self) -> str:
        return f"Rolls removed: {self.removed_rolls}"


def main():
    diagram = read_input(join(dirname(__file__), "input.txt"),
                         lambda line: [x for x in line])
    paper_diagram = PaperDiagram(diagram)
    paper_diagram.remove_all_accessible_rolls()
    print(paper_diagram)


if __name__ == "__main__":
    main()
