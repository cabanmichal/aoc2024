#!/usr/bin/env python3

from collections import defaultdict

F = "d05.txt"


def find_broken_rule(update, rules):
    visited = set()
    for i, n in enumerate(update):
        visited.add(n)
        must_be_later = rules.get(n)
        if not must_be_later:
            continue
        failures = visited & must_be_later
        if failures:
            return i, failures

    return -1, set()


def is_update_valid(update, rules):
    return find_broken_rule(update, rules)[0] == -1


def recover_update(update, rules):
    i, failures = find_broken_rule(update, rules)
    while i > -1:
        j = min(update.index(f) for f in failures)
        update[i], update[j] = update[j], update[i]
        i, failures = find_broken_rule(update, rules)

    return update


def load_rules(rules_string):
    rules = defaultdict(set)
    for line in rules_string.split("\n"):
        line = line.strip()
        if not line:
            continue
        a, b = [int(n) for n in line.split("|")]
        rules[a].add(b)

    return rules


def load_updates(updates_string):
    updates = []
    for line in updates_string.split("\n"):
        line = line.strip()
        if line:
            updates.append([int(n) for n in line.split(",")])

    return updates


def solution1(updates, rules):
    total = 0
    for update in updates:
        if is_update_valid(update, rules):
            total += update[len(update) // 2]

    return total


def solution2(updates, rules):
    total = 0
    for update in updates:
        if is_update_valid(update, rules):
            continue
        update = recover_update(update, rules)
        total += update[len(update) // 2]

    return total


def main():
    with open(F) as fh:
        rules_string, updates_string = fh.read().split("\n\n")
    rules = load_rules(rules_string)
    updates = load_updates(updates_string)

    print(solution1(updates, rules))  # 7074
    print(solution2(updates, rules))  # 4828


if __name__ == "__main__":
    main()
