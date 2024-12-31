from collections import defaultdict
from itertools import combinations

from ..utils import parse_data


def parse_map(input_data):
    antennas = defaultdict(list)
    map_locations = set()
    for y, row in enumerate(input_data):
        for x, c in enumerate(row):
            map_locations.add((x, y))
            if c not in [".", "#"]:
                antennas[c].append((x, y))

    return antennas, map_locations


def solve_part1(data: str):
    input_data = parse_data(data)
    antennas, map_locations = parse_map(input_data)

    antinodes = set()
    for frequency, ant_locations in antennas.items():
        for a, b in combinations(sorted(ant_locations), 2):
            diff = (b[0] - a[0], b[1] - a[1])
            if (aa := (a[0] - diff[0], a[1] - diff[1])) in map_locations:
                antinodes.add(aa)
            if (bb := (b[0] + diff[0], b[1] + diff[1])) in map_locations:
                antinodes.add(bb)

    return len(antinodes)


def solve_part2(data: str):
    input_data = parse_data(data)
    antennas, map_locations = parse_map(input_data)

    antinodes = set()
    for frequency, ant_locations in antennas.items():
        for a, b in combinations(sorted(ant_locations), 2):
            diff = (b[0] - a[0], b[1] - a[1])
            while a in map_locations:
                antinodes.add(a)
                a = (a[0] - diff[0], a[1] - diff[1])
            while b in map_locations:
                antinodes.add(b)
                b = (b[0] + diff[0], b[1] + diff[1])

    return len(antinodes)
