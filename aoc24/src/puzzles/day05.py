from functools import cmp_to_key
from itertools import combinations
from collections import defaultdict

from ..utils import parse_data

def parse_rules_and_updates(data: list[str]):
    input_iter = iter(data)
    rules = set()
    while row := next(input_iter).strip():
        rules.add(tuple(map(int, row.split('|'))))

    updates = [list(map(int, row.split(','))) for row in input_iter]
    return rules, updates

def is_sorted(update, rules):
    return {(c[1],c[0]) for c in combinations(update, 2)} & rules == set()


def midpoint(update):
    return update[len(update)//2]


def solve_part1(data: str):
    input_data = parse_data(data)
    rules, updates = parse_rules_and_updates(input_data)
    correct_updates = [update for update in updates if is_sorted(update, rules)]
    return sum(midpoint(u) for u in correct_updates)


def solve_part2(data: str):
    input_data = parse_data(data)
    rules, updates = parse_rules_and_updates(input_data)
    incorrect_updates = [update for update in updates if not is_sorted(update, rules)]

    lt = defaultdict(set)
    for x, y in rules:
        lt[x].add(y)

    def compare(a, b):
        return 0 if a not in lt else -1 if b in lt[a] else 1

    sorted_updates = [list(sorted(update, key=cmp_to_key(compare))) for update in incorrect_updates]
    return sum(midpoint(u) for u in sorted_updates)
