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


def solution(equations, operators):
    total_result = 0
    for result, numbers in equations:
        for operator_group in product(operators, repeat=len(numbers) - 1):
            subresult = numbers[0]
            for operator, n in zip(operator_group, numbers[1:]):
                subresult = operator(subresult, n)
            if subresult == result:
                total_result += result
                break

    return total_result


def main():
    equations = load_equations(F)

    operators = OPERATORS.copy()
    print(solution(equations, operators))  # 2314935962622

    operators.append(lambda x, y: int(str(x) + str(y)))
    print(solution(equations, operators))  # 401477450831495


if __name__ == "__main__":
    main()
