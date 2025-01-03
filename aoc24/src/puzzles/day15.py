from typing import Literal

from ..utils import parse_data

DIRECTION = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

CardinalDirection = Literal["^", ">", "v", "<"]


class Position:
    def __init__(self, coords: tuple[int, int]):
        self.x = coords[0]
        self.y = coords[1]

    def __hash__(self):
        return hash((self.x, self.y))

    def __getitem__(self, direction: CardinalDirection):
        dx, dy = DIRECTION[direction]
        return Position((self.x + dx, self.y + dy))

    def __eq__(self, other):
        if isinstance(other, tuple):
            return (self.x, self.y) == other
        return (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Puzzle1:
    def __init__(self, data: list[str]):
        input_iter = iter(data)
        self.walls = set()
        self.boxes = set()
        self.directions = list()

        y = 0
        while (row := next(input_iter)) != "":
            for x, c in enumerate(row):
                if c == "@":
                    self.robot = Position((x, y))
                elif c == "#":
                    self.walls.add(Position((x, y)))
                elif c == "O":
                    self.boxes.add(Position((x, y)))
            y += 1

        self.size = (
            max([p.x for p in self.walls]) + 1,
            max([p.y for p in self.walls]) + 1,
        )

        while row := next(input_iter, None):
            self.directions.extend([c for c in row])

    def can_move(self, start: Position, direction: CardinalDirection):
        next_location = start[direction]
        if next_location in self.walls or (
            next_location in self.boxes and not self.can_move(next_location, direction)
        ):
            return False

        if start in self.boxes:
            self.boxes.remove(start)
            self.boxes.add(next_location)
        return True

    def play(self):
        for d in self.directions:
            if self.can_move(self.robot, d):
                self.robot = self.robot[d]

        return sum([box.x + box.y * 100 for box in self.boxes])


def solve_part1(data: str):
    input_data = parse_data(data)
    return Puzzle1(input_data).play()


def solve_part2(data: str):
    input_data = parse_data(data)
    return None
