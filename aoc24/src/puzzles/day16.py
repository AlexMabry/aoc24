from functools import reduce
from itertools import pairwise

import networkx as nx

from ..utils import parse_data


def build_graph(grid):
    positions = {(x, y) for (x, y), v in grid.items() if v in [".", "E", "S"]}
    nodes = {(x, y, d) for (x, y) in positions for d in ["N", "E", "S", "W"]}

    G = nx.DiGraph()
    G.add_nodes_from(nodes)

    # Add 90 deg turns
    for x, y in positions:
        for a, b in pairwise(["N", "E", "S", "W", "N"]):
            G.add_edge((x, y, a), (x, y, b), weight=1000)
            G.add_edge((x, y, b), (x, y, a), weight=1000)

    # Add edges
    for x, y in positions:
        if (x, y - 1) in positions:
            G.add_edge((x, y, "N"), (x, y - 1, "N"), weight=1)
        if (x, y + 1) in positions:
            G.add_edge((x, y, "S"), (x, y + 1, "S"), weight=1)
        if (x - 1, y) in positions:
            G.add_edge((x, y, "W"), (x - 1, y, "W"), weight=1)
        if (x + 1, y) in positions:
            G.add_edge((x, y, "E"), (x + 1, y, "E"), weight=1)

    sx, sy = next(k for k, v in grid.items() if v == "S")
    ex, ey = next(k for k, v in grid.items() if v == "E")

    return G, (sx, sy, "E"), [(ex, ey, d) for d in "NESW"]


def shortest_path(G, start, ends):
    return min([(nx.dijkstra_path_length(G, start, end), end) for end in ends])


def solve_part1(data: str):
    parsed = parse_data(data)
    grid = {(x, y): c for y, row in enumerate(parsed) for x, c in enumerate(row)}
    G, start, ends = build_graph(grid)
    return shortest_path(G, start, ends)[0]


def solve_part2(data: str):
    parsed = parse_data(data)
    grid = {(x, y): c for y, row in enumerate(parsed) for x, c in enumerate(row)}

    G, start, ends = build_graph(grid)
    _, end = shortest_path(G, start, ends)

    best_paths = [
        {(x, y) for x, y, d in p}
        for p in nx.all_shortest_paths(G, start, end, weight="weight")
    ]
    return len(reduce(set.union, best_paths))
