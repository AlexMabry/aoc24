from functools import reduce

from black.trans import defaultdict

from ..utils import parse_data


def get_left_right(input_data):
    walk_numbers = (tuple(int(x) for x in row.split("   ")) for row in input_data)
    left, right = [], []

    for l, r in walk_numbers:
        left.append(l)
        right.append(r)

    return left, right

def solve_part1(data: str):
    input_data = parse_data(data)
    left, right = get_left_right(input_data)

    return sum([abs(l - r) for l, r in zip(sorted(left), sorted(right))])


def count_appearance(d, n):
    d[n] += 1
    return d


def solve_part2(data: str):
    input_data = parse_data(data)
    left, right = get_left_right(input_data)

    count = reduce(count_appearance, right, defaultdict(int))
    return sum([num*count[num] for num in left])
