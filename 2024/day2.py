
def is_safe(diff):
    all_positive = not any([x for x in diff if x < 0])
    all_negative = not any([x for x in diff if x > 0])
    has_zero = 0 in diff
    high_rate_of_change = any([x for x in diff if abs(x) < 1 or abs(x) > 3])

    return (not high_rate_of_change) and (all_positive or all_negative) and (not has_zero)

def calc_diff(levels):
    return [int(x[0]) - int(x[1]) for x in zip(levels, levels[1:])]

safe_lines_count = 0

with open("2024/day2.txt", "r") as f:
    for line in f.readlines():
        levels = line.strip().split()
        
        diff = calc_diff(levels)
        
        if is_safe(diff):
            safe_lines_count += 1
        else:
            for i, _ in enumerate(levels):
                test_level = levels[:i] + levels[i+1:]
                test_level_diff = calc_diff(test_level)
                if is_safe(test_level_diff):
                    safe_lines_count += 1
                    break
        
        
print(safe_lines_count)