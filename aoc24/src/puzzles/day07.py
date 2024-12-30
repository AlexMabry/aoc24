from ..utils import parse_data


def parse_problems(input_data):
    problems = []
    for line in input_data:
        value, numbers = line.split(": ")
        problems.append((int(value), [int(x) for x in numbers.split(" ")]))
    return problems


def is_valid_1(value, numbers):
    if len(numbers) == 1:
        return value == numbers[0]
    last = numbers.pop()
    possibilities = [is_valid_1(value - last, list(numbers))]
    if value % last == 0:
        possibilities.append(is_valid_1(value // last, list(numbers)))

    return any(possibilities)


def solve_part1(data: str):
    input_data = parse_data(data)
    problems = parse_problems(input_data)

    return sum([value for value, numbers in problems if is_valid_1(value, numbers)])


def is_valid_2(value, numbers):
    if value <= 0:
        return False
    if len(numbers) == 1:
        return value == numbers[0]
    last = numbers.pop()
    possibilities = [is_valid_2(value - last, list(numbers))]
    if value % last == 0:
        possibilities.append(is_valid_2(value // last, list(numbers)))
    if str(value).endswith(str(last)) and len(str(value)) > len(str(last)):
        value = int(str(value)[: -len(str(last))])
        possibilities.append(is_valid_2(value, list(numbers)))

    return any(possibilities)


def solve_part2(data: str):
    input_data = parse_data(data)
    problems = parse_problems(input_data)

    return sum([value for value, numbers in problems if is_valid_2(value, numbers)])
