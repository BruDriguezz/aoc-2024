def assert_safety(report: str) -> bool:
    levels = list(map(int, report.split()))
    direction = None

    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if not (1 <= abs(diff) <= 3):  
            return False
        current_direction = diff > 0
        if direction is None:
            direction = current_direction
        elif direction != current_direction:
            return False
    return True

def assert_safety_with_dampener(report: str) -> bool:
    levels = list(map(int, report.split()))
    if assert_safety(report):
        return True
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if assert_safety(" ".join(map(str, modified_levels))):
            return True
    return False

with open("./input.txt") as file:
    totals = 0
    for report in file:
        if assert_safety_with_dampener(report.strip()):
            totals += 1

    print(totals)


with open("./input.txt") as file:
    totals = 0
    for report in file.readlines():
        is_safe = assert_safety(report)

        if is_safe:
            totals += 1
        else:
            continue
    print(totals)
