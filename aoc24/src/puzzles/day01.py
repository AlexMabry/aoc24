from ..utils import parse_data


def solve_part1(data: str):
    input_data = parse_data(data)
    walk_numbers = (tuple(int(x) for x in row.split("   ")) for row in input_data)

    left, right = [], []
    for l, r in walk_numbers:
        left.append(l)
        right.append(r)

    total_diff = 0
    for l, r in zip(sorted(left), sorted(right)):
        total_diff += abs(l - r)

    return total_diff


def solve_part2(data: str):
    input_data = parse_data(data)
    print(input_data)

    return None
