import math
from os.path import dirname, join
from utils import read_input


class JunctionBox:
    def __init__(self, coordinates: str):
        self.id = coordinates
        self.coordinates = [int(x) for x in coordinates.split(",")]


class LightSetup:
    def __init__(self, boxes: list[JunctionBox]):
        self.junction_boxes = boxes
        self.box_distances: dict[str, int] = {}
        self.circuits: list[set[str]] = []

    def find_box_distances(self) -> None:
        for i, box1 in enumerate(self.junction_boxes[:-1]):
            for box2 in self.junction_boxes[i + 1:]:
                self.box_distances[f"{box1.id}|{box2.id}"] = math.dist(
                    box1.coordinates, box2.coordinates)

        self.box_distances = dict(
            sorted(self.box_distances.items(), key=lambda item: item[1]))

    def add_connection(self, connection: tuple[str, int]) -> None:
        circuits_to_merge = []
        boxes = connection[0].split("|")
        for index, circuit in enumerate(self.circuits):
            if circuit.intersection(set(boxes)):
                circuits_to_merge.append(index)
                if len(circuits_to_merge) == 2:
                    break

        if len(circuits_to_merge) == 1:
            first_circuit = self.circuits[circuits_to_merge[0]]
            first_circuit |= set(boxes)
            return

        if len(circuits_to_merge) == 2:
            first_circuit = self.circuits[circuits_to_merge[0]]
            second_circuit = self.circuits.pop(circuits_to_merge[1])
            first_circuit |= second_circuit | set(boxes)
            return

        self.circuits.append(set(boxes))

    def connect_closest_boxes(self, count: int = 1000) -> None:
        for connection in list(self.box_distances.items())[:count]:
            self.add_connection(connection)

    def connect_closest_boxes_until_all_connected(self) -> str:
        for index, connection in enumerate(list(self.box_distances.items())):
            self.add_connection(connection)
            if len(self.circuits) == 1 and not self.circuits[0] ^ set([box.id for box in self.junction_boxes]):
                return connection[0]

        return self.box_distances[0][0]

    def multiply_three_largest_circuits(self) -> int:
        circuit_sizes = [len(circuit) for circuit in self.circuits]
        circuit_sizes.sort(reverse=True)

        product = 1
        for size in circuit_sizes[:3]:
            product *= size

        return product

    def multiply_x_coords_of_connection(self, connection: str) -> int:
        boxes = connection.split("|")
        coords = [box.split(",") for box in boxes]
        x_coords = [int(coord[0]) for coord in coords]
        return x_coords[0] * x_coords[1]


def main():
    boxes = read_input(join(dirname(__file__), "input.txt"),
                       lambda line: JunctionBox(line))

    light_setup = LightSetup(boxes)
    light_setup.find_box_distances()
    final_connection = light_setup.connect_closest_boxes_until_all_connected()

    print(light_setup.multiply_x_coords_of_connection(final_connection))


if __name__ == "__main__":
    main()
