from collections import deque
from itertools import batched

from ..utils import parse_data


def parse_disk_map(input_data):
    return [int(c) for c in input_data[0]]


def expand_disk_map(disk_map):
    ptr = 0
    taken, empty = deque(), []
    for file_id, (disk, free) in enumerate(batched(disk_map[:-1], n=2)):
        for i in range(disk):
            taken.append((ptr, file_id))
            ptr += 1
        for i in range(free):
            empty.append(ptr)
            ptr += 1
    for i in range(disk_map[-1]):
        taken.append((ptr, file_id + 1))
        ptr += 1

    return taken, empty


def solve_part1(data: str):
    input_data = parse_data(data)
    disk_map = parse_disk_map(input_data)
    taken, empty_spots = expand_disk_map(disk_map)

    checksum, ptr = 0, 0
    for need_to_fill in empty_spots:
        while taken and ptr < need_to_fill:
            front_ptr = taken.popleft()
            checksum += front_ptr[0] * front_ptr[1]
            ptr += 1

        if taken:
            back_ptr = taken.pop()
            checksum += need_to_fill * back_ptr[1]
            ptr += 1

    return checksum


def solve_part2(data: str):
    input_data = parse_data(data)
    print(input_data)

    return None