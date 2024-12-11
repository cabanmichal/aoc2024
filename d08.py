#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations

F = "d08.txt"


def load_grid(f):
    rows = []
    with open(f) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rows.append(list(line))

    return rows


def is_location_in_grid(grid, location):
    r, c = location
    return 0 <= r < len(grid) and 0 <= c < len(grid[r])


def is_antena(character):
    return character.isalnum()


def group_antenas_by_freq(grid):
    group = defaultdict(list)

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if is_antena(col):
                group[col].append((r, c))

    return group


def get_antinodes_of_two_antenas(grid, position1, position2):
    r1, c1 = position1
    r2, c2 = position2

    ra1 = r1 + (r1 - r2)
    ra2 = r2 + (r2 - r1)
    ca1 = c1 + (c1 - c2)
    ca2 = c2 + (c2 - c1)

    antinodes = []
    for location in [(ra1, ca1), (ra2, ca2)]:
        if is_location_in_grid(grid, location):
            antinodes.append(location)

    return antinodes


def get_antinodes_in_line(grid, position1, position2):
    r1, c1 = position1
    r2, c2 = position2
    r_diff_1 = r1 - r2
    r_diff_2 = r2 - r1
    c_diff_1 = c1 - c2
    c_diff_2 = c2 - c1
    antinodes = [position1, position2]

    while True:
        r1 += r_diff_1
        c1 += c_diff_1
        location = (r1, c1)
        if not is_location_in_grid(grid, location):
            break

        antinodes.append(location)

    while True:
        r2 += r_diff_2
        c2 += c_diff_2
        location = (r2, c2)
        if not is_location_in_grid(grid, location):
            break

        antinodes.append(location)

    return antinodes


def solution(grid, antinodes_finder_func):
    unique_antinodes = set()
    for group in group_antenas_by_freq(grid).values():
        for pair in combinations(group, 2):
            for antinode in antinodes_finder_func(grid, *pair):
                unique_antinodes.add(antinode)

    return len(unique_antinodes)


def main():
    grid = load_grid(F)
    print(solution(grid, get_antinodes_of_two_antenas))  # 265
    print(solution(grid, get_antinodes_in_line))  # 962


if __name__ == "__main__":
    main()
