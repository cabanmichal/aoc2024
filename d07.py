#!/usr/bin/env python3

from itertools import product
import operator as op

F = "d07.txt"

OPERATORS = [op.mul, op.add]


def load_equations(f):
    equations = []

    with open(f) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            result, numbers = line.split(": ")
            equations.append((int(result), [int(n) for n in numbers.split(" ")]))

    return equations


def equation_valid(result, numbers, operators):
    for op_arrangement in product(operators, repeat=len(numbers) - 1):
        subresult = numbers[0]
        for operator, n in zip(op_arrangement, numbers[1:]):
            subresult = operator(subresult, n)
        if subresult == result:
            return True

    return False


def solution(equations, operators, use_concat):
    total_result = 0
    op_extended = operators + [lambda x, y: int(str(x) + str(y))]

    for result, numbers in equations:
        if (
            equation_valid(result, numbers, operators)
            or use_concat
            and equation_valid(result, numbers, op_extended)
        ):
            total_result += result

    return total_result


def main():
    equations = load_equations(F)
    print(solution(equations, OPERATORS, False))  # 2314935962622
    print(solution(equations, OPERATORS, True))  # 401477450831495


if __name__ == "__main__":
    main()
