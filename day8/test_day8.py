import pytest
from day8.day8 import *

sample_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


sample_boxes = [JunctionBox(line) for line in sample_input.split()]


def test_light_setup_find_box_distances__when_sample_input__expect_first_162_817_812_425_690_689():
    light_setup = LightSetup(sample_boxes)
    expected = "162,817,812|425,690,689"

    light_setup.find_box_distances()

    assert list(light_setup.box_distances.keys())[0] == expected


def test_light_setup_add_connection__when_empty__expect_new_circuit():
    light_setup = LightSetup([])
    expected = [set(["1,2,3", "4,5,6"])]

    light_setup.add_connection(("1,2,3|4,5,6", 1))

    assert expected == light_setup.circuits


def test_light_setup_add_connection__when_first_value_exists__expect_add_second_value():
    light_setup = LightSetup([])
    light_setup.circuits = [set(["1,2,3"])]
    expected = [set(["1,2,3", "4,5,6"])]

    light_setup.add_connection(("1,2,3|4,5,6", 1))

    assert expected == light_setup.circuits


def test_light_setup_add_connection__when_second_value_exists__expect_add_first_value():
    light_setup = LightSetup([])
    light_setup.circuits = [set(["4,5,6"])]
    expected = [set(["1,2,3", "4,5,6"])]

    light_setup.add_connection(("1,2,3|4,5,6", 1))

    assert expected == light_setup.circuits


def test_light_setup_add_connection__when_both_values_exist__expect_nothing_added():
    light_setup = LightSetup([])
    light_setup.circuits = [set(["1,2,3", "4,5,6"])]
    expected = [set(["1,2,3", "4,5,6"])]

    light_setup.add_connection(("1,2,3|4,5,6", 1))

    assert expected == light_setup.circuits


def test_light_setup_add_connection__when_no_values_exist__expect_new_set():
    light_setup = LightSetup([])
    light_setup.circuits = [set(["7,8,9"])]
    expected = [set(["7,8,9"]), set(["1,2,3", "4,5,6"])]

    light_setup.add_connection(("1,2,3|4,5,6", 1))

    assert expected == light_setup.circuits


def test_light_setup_multiply_three_largest_circuits__when_sample_input__expect_40():
    light_setup = LightSetup(sample_boxes)
    expected = 40

    light_setup.find_box_distances()
    light_setup.connect_closest_boxes(10)
    actual = light_setup.multiply_three_largest_circuits()

    assert expected == actual


def test_part_2__when_sample_input__expect_40():
    light_setup = LightSetup(sample_boxes)
    expected = 25272

    light_setup.find_box_distances()
    final_connection = light_setup.connect_closest_boxes_until_all_connected()
    actual = light_setup.multiply_x_coords_of_connection(final_connection)

    assert expected == actual
