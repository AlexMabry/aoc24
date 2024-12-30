from ..utils import parse_data

N, E, S, W = (0, -1), (1, 0), (0, 1), (-1, 0)
TURN = {N: E, E: S, S: W, W: N}


def look_ahead(guard, direction):
    return guard[0] + direction[0], guard[1] + direction[1]


def parse_floor(input_data):
    floor, obstructions, location = set(), set(), None
    for y, row in enumerate(input_data):
        for x, c in enumerate(row):
            if c == "^":
                location = (x, y)
            if c != "#":
                floor.add((x, y))
            else:
                obstructions.add((x, y))

    return floor, obstructions, location


def create_path(floor, obstructions, location, direction=N):
    path = set()
    while location in floor:
        if (location, direction) in path:
            return None  # Loop detected

        path.add((location, direction))
        if (next_step := look_ahead(location, direction)) in obstructions:
            direction = TURN[direction]
        else:
            location = next_step

    return path


def solve_part1(data: str):
    input_data = parse_data(data)
    floor, obstructions, location = parse_floor(input_data)
    path = create_path(floor, obstructions, location)

    return len({location for location, _ in path})


def solve_part2(data: str):
    input_data = parse_data(data)
    floor, obstructions, guard = parse_floor(input_data)
    path = create_path(floor, obstructions, guard)

    new_obstructions = set()
    for location, direction in path:
        next_step = look_ahead(location, direction)
        if (
            next_step in floor
            and next_step not in new_obstructions
            and not create_path(floor - {next_step}, obstructions | {next_step}, guard)
        ):
            new_obstructions.add(next_step)

    return len(new_obstructions)
