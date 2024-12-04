#!/usr/bin/env python3

F = "d03.txt"
MUL_EX_START = "mul("
DO_EX_START = "do("
DONT_EX_START = "don't("
EX_END = ")"


def get_expr(s, ex_start, ex_end, ex_arg_f):
    j = 0
    while j < len(s):
        i = s.find(ex_start, j)
        if i == -1:
            return None
        j = i + len(ex_start)
        while j < len(s) and ex_arg_f(s[j]):
            j += 1
            continue
        if j < len(s) and s[j] == ex_end:
            j += 1
            yield i, s[i:j]


def eval_mul_expr(expr):
    expr = expr.replace(MUL_EX_START, "").replace(EX_END, "")
    a, b = [int(n) for n in expr.split(",")]

    return a * b


def mem_result(mem, ignore_dos_donts):
    expressions = list(
        get_expr(mem, MUL_EX_START, EX_END, lambda x: x.isdigit() or x == ",")
    )
    if not ignore_dos_donts:
        expressions += list(get_expr(mem, DO_EX_START, EX_END, lambda x: False))
        expressions += list(get_expr(mem, DONT_EX_START, EX_END, lambda x: False))
        expressions.sort()

    total = 0
    should_multiply = True
    for _, expr in expressions:
        if expr.startswith(MUL_EX_START):
            if should_multiply:
                total += eval_mul_expr(expr)
        elif expr.startswith(DONT_EX_START):
            should_multiply = False
        else:
            should_multiply = True

    return total


if __name__ == "__main__":
    with open(F) as fh:
        mem = fh.read()

    print(mem_result(mem, True))  # 184576302
    print(mem_result(mem, False))  # 118173507
