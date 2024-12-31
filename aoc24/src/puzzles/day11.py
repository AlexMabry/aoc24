from functools import reduce, cache

from ..utils import parse_data


def blink(acc: list, x: int):
    if x == 0:
        acc.append(1)
    elif len(str_x := str(x)) % 2 == 0:
        acc.extend([int(str_x[: len(str_x) // 2]), int(str_x[len(str_x) // 2 :])])
    else:
        acc.append(x * 2024)

    return acc


def solve_part1(data: str):
    input_data = parse_data(data)
    stones = list(map(int, input_data[0].split(" ")))
    for i in range(25):
        stones = list(reduce(blink, stones, []))

    return len(stones)


@cache
def solve_subproblem(stone: int, turns: int):
    if turns == 0:
        return 1

    if stone == 0:
        return solve_subproblem(1, turns - 1)
    elif len(str_stone := str(stone)) % 2 == 0:
        return solve_subproblem(
            int(str_stone[: len(str_stone) // 2]), turns - 1
        ) + solve_subproblem(int(str_stone[len(str_stone) // 2 :]), turns - 1)
    else:
        return solve_subproblem(stone * 2024, turns - 1)


def solve_part2(data: str):
    input_data = parse_data(data)
    stones = list(map(int, input_data[0].split(" ")))
    return sum(solve_subproblem(stone, 75) for stone in stones)
