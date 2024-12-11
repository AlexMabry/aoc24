import sys
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

YEAR = 2024
START_DAY = 1
END_DAY = 25

PACKAGE = f"aoc{YEAR%100}"


def generate():
    cwd = Path.cwd()

    src_dir = cwd / PACKAGE / "src"
    src_dir.mkdir(exist_ok=True)

    puzzle_dir = src_dir / "puzzles"
    puzzle_dir.mkdir(exist_ok=True)

    puzzle_init = puzzle_dir / "__init__.py"
    puzzle_init.touch()

    loader = FileSystemLoader(cwd / PACKAGE / "templates")
    env = Environment(loader=loader)
    template = env.get_template("aocd_problem.j2")

    for day in range(START_DAY, (END_DAY + 1), 1):
        day_py = puzzle_dir / f"day{day:02}.py"
        day_py.touch()
        day_py.write_text(template.render() + "\n")


if __name__ == "__main__":
    generate()
