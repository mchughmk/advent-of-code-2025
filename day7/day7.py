from collections import defaultdict
from os.path import dirname, join
from utils import read_input


def find_start_index(start_row: list[str]) -> int:
    return start_row.index("S")


def count_splits(diagram: list[list[str]]) -> int:
    num_splits = 0

    start_index = find_start_index(diagram[0])
    beams = set([start_index])

    for row in diagram[1:]:
        for beam in list(beams):
            if row[beam] == "^":
                num_splits += 1
                beams.remove(beam)
                beams.update([beam - 1, beam + 1])

    return num_splits


def count_timelines(diagram: list[list[str]]) -> int:
    timelines = 1

    start_index = find_start_index(diagram[0])
    beams = defaultdict(int)
    beams[start_index] += 1

    for row in diagram[1:]:
        for beam in list(beams.keys()):
            if row[beam] == "^":
                timelines += beams[beam]
                beams[beam-1] += beams[beam]
                beams[beam+1] += beams[beam]
                del beams[beam]

    return timelines


def main():
    diagram = read_input(join(dirname(__file__), "input.txt"),
                         lambda line: [x for x in line])

    print(count_timelines(diagram))


if __name__ == "__main__":
    main()
