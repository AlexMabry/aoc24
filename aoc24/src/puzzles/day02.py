from ..utils import parse_data


def is_safe(report):
    diff = [num - report[ix] for ix, num in enumerate(report[1:])]
    return 0 < max(diff) <= 3 and min(diff) > 0 or -3 <= min(diff) < 0 and max(diff) < 0


def removing_one(report):
    return (report[:ix] + report[ix + 1 :] for ix, x in enumerate(report))


def is_subset_safe(report):
    return any(is_safe(version) for version in removing_one(report))


def solve_part1(data: str):
    input_data = parse_data(data)
    reports = [[int(x) for x in row.split(" ")] for row in input_data]

    return len([r for r in reports if is_safe(r)])


def solve_part2(data: str):
    input_data = parse_data(data)
    reports = [[int(x) for x in row.split(" ")] for row in input_data]

    return len([r for r in reports if is_safe(r) or is_subset_safe(r)])
