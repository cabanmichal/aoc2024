#!/usr/bin/env python3

F = "d02.txt"


def is_report_safe(report, diff_min, diff_max):
    incr = True
    decr = True
    i = 0
    while i < len(report) - 1:
        a, b = report[i : i + 2]
        incr = incr and (a > b)
        decr = decr and (a < b)
        if not (incr or decr):
            return False, i

        if not diff_min <= abs(a - b) <= diff_max:
            return False, i

        i += 1

    return True, -1


def count_safe_reports(reports, diff_min, diff_max, allow_error):
    safe_reports = 0
    for report in reports:
        ok, i = is_report_safe(report, diff_min, diff_max)
        if ok:
            safe_reports += 1
        elif allow_error:
            for offset in (0, 1, -1):
                adjusted = [v for j, v in enumerate(report) if j != i + offset]
                if is_report_safe(adjusted, diff_min, diff_max)[0]:
                    safe_reports += 1
                    break

    return safe_reports


if __name__ == "__main__":
    diff_min = 1
    diff_max = 3

    reports = []
    with open(F) as fh:
        for line in fh:
            report = [int(n) for n in line.strip().split()]
            if report:
                reports.append(report)

    print(count_safe_reports(reports, diff_min, diff_max, False))  # 516
    print(count_safe_reports(reports, diff_min, diff_max, True))  # 561
