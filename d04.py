#!/usr/bin/env python3

F = "d04.txt"
WORD1 = "XMAS"
WORD2 = "MAS"
DIRECTIONS = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]


def get_positions_in_direction(position, direction, count):
    positions = []
    x, y = position
    dx, dy = direction

    for c in range(1, count + 1):
        positions.append((x + c * dx, y + c * dy))

    return positions


def solution1(puzzle):
    word_count = 0
    for row, line in enumerate(puzzle):
        for pos, letter in enumerate(line):
            if letter != WORD1[0]:
                continue
            for direction in DIRECTIONS:
                positions = get_positions_in_direction(
                    (pos, row), direction, len(WORD1) - 1
                )
                word = [letter]
                for x, y in positions:
                    if x < 0 or x >= len(line) or y < 0 or y >= len(puzzle):
                        break
                    word.append(puzzle[y][x])
                else:
                    if "".join(word) == WORD1:
                        word_count += 1

    return word_count


def solution2(puzzle):
    word_count = 0
    for row, line in enumerate(puzzle):
        if row == 0 or row == len(puzzle) - 1:
            continue
        for pos, letter in enumerate(line):
            if letter != WORD2[1] or pos == 0 or pos == len(line) - 1:
                continue
            tl = puzzle[row - 1][pos - 1]
            br = puzzle[row + 1][pos + 1]
            tr = puzzle[row - 1][pos + 1]
            bl = puzzle[row + 1][pos - 1]
            if (
                all(ch == WORD2[0] or ch == WORD2[2] for ch in [tl, br, tr, bl])
                and tl != br
                and tr != bl
            ):
                word_count += 1

    return word_count


if __name__ == "__main__":
    with open(F) as fh:
        puzzle = []
        for line in fh:
            line = line.strip()
            if line:
                puzzle.append(line)

    print(solution1(puzzle))  # 2517
    print(solution2(puzzle))  # 1960
