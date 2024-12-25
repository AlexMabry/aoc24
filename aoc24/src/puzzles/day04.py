from ..utils import parse_data

NEIGHBORS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
DIAGONALS = [(1, 1), (1, -1)]


def solve_part1(data: str):
    input_data = parse_data(data)
    grid = {(x, y): c for y, row in enumerate(input_data) for x, c in enumerate(row)}
    xmas = [{pt for pt in grid if grid[pt] == letter} for letter in "XMAS"]

    return sum(
        all(
            (x + dx * offset, y + dy * offset) in letter
            for offset, letter in enumerate(xmas[1:], 1)
        )
        for x, y in xmas[0]
        for dx, dy in NEIGHBORS
    )


def solve_part2(data: str):
    input_data = parse_data(data)
    grid = {(x, y): c for y, row in enumerate(input_data) for x, c in enumerate(row)}
    _, M, A, S = [{pt for pt in grid if grid[pt] == letter} for letter in "XMAS"]

    crosses = [
        [((x + dx, y + dy), (x - dx, y - dy)) for dx, dy in DIAGONALS] for x, y in A
    ]

    return sum(
        all(p1 in M and p2 in S or p1 in S and p2 in M for p1, p2 in legs)
        for legs in crosses
    )
