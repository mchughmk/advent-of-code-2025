from os.path import dirname, join
from shapely import Point, Polygon, box
from utils import read_input


def find_area(point1: Point, point2: Point):
    length = abs(point1.x - point2.x) + 1
    height = abs(point1.y - point2.y) + 1
    return length * height


def create_square(point1, point2):
    xmin = xmax = ymin = ymax = 0

    if point1.x < point2.x:
        xmin = point1.x
        xmax = point2.x
    else:
        xmin = point2.x
        xmax = point1.x

    if point1.y < point2.y:
        ymin = point1.y
        ymax = point2.y
    else:
        ymin = point2.y
        ymax = point1.y

    return box(xmin, ymin, xmax, ymax)


def find_largest_rectangle(points: list[Point]):
    largest_area = 0
    for index, point1 in enumerate(points[:-1]):
        for point2 in points[index+1:]:
            area = find_area(point1, point2)
            if area > largest_area:
                largest_area = area

    return largest_area


def find_largest_green_rectangle(points: list[Point]):
    shape = Polygon(points + [points[0]])
    largest_area = 0
    for index, point1 in enumerate(points[:-1]):
        for point2 in points[index+1:]:
            square = create_square(point1, point2)
            if shape.contains(square):
                area = find_area(point1, point2)
                if area > largest_area:
                    largest_area = area

    return largest_area


def main():
    points = read_input(join(dirname(__file__), "input.txt"),
                        lambda line: Point(*line.split(",")))

    print(find_largest_green_rectangle(points))


if __name__ == "__main__":
    main()
