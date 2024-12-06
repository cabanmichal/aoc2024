#!/usr/bin/env python3

F = "d06.txt"
OBSTACLE = "#"
SHAPES = "^>v<"
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def load_map():
    m = []
    with open(F) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            m.append(list(line))

    return m


def find_guard(area_map):
    for i, row in enumerate(area_map):
        for j, col in enumerate(row):
            if area_map[i][j] in SHAPES:
                direction = DIRECTIONS[SHAPES.index(area_map[i][j])]

                return i, j, *direction

    return -1, -1, -1, -1


def get_guard_path(area_map):
    path = [find_guard(area_map)]
    visited = set(path)

    r, c, dr, dc = path[0]
    direction_index = DIRECTIONS.index((dr, dc))

    while True:
        next_r = r + dr
        next_c = c + dc
        if 0 <= next_r < len(area_map) and 0 <= next_c < len(area_map[0]):
            if area_map[next_r][next_c] == OBSTACLE:
                direction_index = (direction_index + 1) % len(DIRECTIONS)
                dr, dc = DIRECTIONS[direction_index]
            else:
                r = next_r
                c = next_c
                path.append((r, c, dr, dc))
                if path[-1] in visited:  # cycle
                    return path, True
                visited.add(path[-1])
        else:
            break

    return path, False


def main():
    area_map = load_map()
    path, _ = get_guard_path(area_map)
    unique_positions = {(r, c) for r, c, *_ in path}

    print(len(unique_positions))  # 4454

    n_of_cycle_positions = 0
    r, c, *_ = path[0]
    unique_positions.remove((r, c))  # no obstacle at start position possible

    for r, c in unique_positions:
        orig_value = area_map[r][c]
        area_map[r][c] = OBSTACLE
        _, cycle = get_guard_path(area_map)
        if cycle:
            n_of_cycle_positions += 1
        area_map[r][c] = orig_value

    print(n_of_cycle_positions)  # 1503


if __name__ == "__main__":
    main()
