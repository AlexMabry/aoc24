import re
from ..utils import parse_data

PATTERN = re.compile(r"mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)|(?P<yes>do)\(\)|(?P<no>don't)\(\)")


def scan_data(data: list[str]):
    for line in data:
        for result in PATTERN.finditer(line):
            yield result.groupdict()


def solve_part1(data: str):
    input_data = parse_data(data)
    answer = 0
    for result in scan_data(input_data):
        if result["a"] and result["b"]:
            answer += int(result["a"]) * int(result["b"])

    return answer



def solve_part2(data: str):
    input_data = parse_data(data)
    answer, enabled = 0, True
    for result in scan_data(input_data):
        if not enabled and result["yes"]:
            enabled = True
        elif enabled and result["no"]:
            enabled = False
        elif enabled and result["a"] and result["b"]:
            answer += int(result["a"]) * int(result["b"])

    return answer
