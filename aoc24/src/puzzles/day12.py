from black.trans import defaultdict

from ..utils import parse_data


def get_neighbors(x, y):
    return {"N": (x, y - 1), "E": (x + 1, y), "S": (x, y + 1), "W": (x - 1, y)}


def find_regions(parsed):
    grid = {(x, y): c for y, row in enumerate(parsed) for x, c in enumerate(row)}
    not_visited = set(grid.keys())
    plot_not_visited = set()
    regions, fences = [], []
    while not_visited:
        while plot_not_visited:
            pt = plot_not_visited.pop()
            regions[-1] += 1
            not_visited.remove(pt)
            for abbr, neighbor in get_neighbors(*pt).items():
                if neighbor not in grid or grid[neighbor] != grid[pt]:
                    fences[-1][abbr].append(pt)

                if neighbor in not_visited and grid[neighbor] == grid[pt]:
                    plot_not_visited.add(neighbor)

        if not_visited:
            regions.append(0)
            fences.append(defaultdict(list))
            plot_not_visited.add(next(iter(not_visited)))

    return zip(regions, fences)


def total_segments(fences):
    return sum(len(segments) for f, segments in fences.items())


def solve_part1(data: str):
    parsed = parse_data(data)
    return sum([area * total_segments(f) for area, f in find_regions(parsed)])


def total_sides(fences):
    return (
        total_segments(fences)
        - len([1 for s in fences["N"] if (s[0] + 1, s[1]) in fences["N"]])
        - len([1 for s in fences["E"] if (s[0], s[1] + 1) in fences["E"]])
        - len([1 for s in fences["S"] if (s[0] - 1, s[1]) in fences["S"]])
        - len([1 for s in fences["W"] if (s[0], s[1] - 1) in fences["W"]])
    )


def solve_part2(data: str):
    parsed = parse_data(data)
    return sum([area * total_sides(f) for area, f in find_regions(parsed)])
