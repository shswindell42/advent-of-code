
 # allow for off by one
def compare(a, b, allowance) -> tuple[bool, int]:
    difference = len([x for x, y in zip(a, b) if x != y])
    return difference <= allowance, difference

def compare_strict(a, b, allowance) -> tuple[bool, int]:
    return a == b, 1


def solve(pattern: list[str], compare) -> int:
    # check rows
    reflectionRow = 0
    for i, line in enumerate(pattern):
        if i+1 < len(pattern):
            reflection = pattern[i+1]
            match, diff = compare(line, reflection, 1)
            allowance = 0 if diff else 1
            if match:
                # check that this is a good reflection
                good_reflection = True
                for j in range(1, i+1):
                    if i - j >= 0 and i + j + 1 < len(pattern):
                        match, diff = compare(pattern[i - j], pattern[i + j + 1], allowance)
                        allowance = 0 if diff or allowance == 0 else 1
                        if not match:
                            good_reflection = False
                            break
                if good_reflection and allowance == 0:
                    reflectionRow = i+1
                    break

    # check columns
    reflectionColumn = 0
    if not reflectionRow:
        for i in range(len(pattern[0])):
            if i + 1 < len(pattern[0]):
                real_line = [s[i] for s in pattern]
                reflection = [s[i + 1] for s in pattern]
                match, diff = compare(real_line, reflection, 1)
                allowance = 0 if diff else 1
                if match:
                    good_reflection = True
                    for j in range(1, i+1):
                        if i - j >= 0 and i + j + 1 < len(pattern[0]):
                            next_real_line = [s[i - j] for s in pattern]
                            next_reflection = [s[i + j + 1] for s in pattern]
                            match, diff = compare(next_real_line, next_reflection, allowance)
                            allowance = 0 if diff or allowance == 0 else 1
                            if not match:
                                good_reflection = False
                                break
                            
                    if good_reflection and allowance == 0:
                        reflectionColumn = i + 1
                        break
                
    return reflectionRow * 100 + reflectionColumn


sum_pattern_notes = 0
patterns = []
pattern = []
with open('./day13.txt', 'r') as fp:
    for line in fp.readlines():
        if line == '\n':
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line.strip())
    
    patterns.append(pattern)

    for pattern in patterns:
        amount = solve(pattern, compare_strict)
        amount_smudge = solve(pattern, compare)
        # if amount == amount_smudge:
        print(f"This scored {amount} and {amount_smudge}:")
        for l in pattern:
            print(l)
        print()
        sum_pattern_notes += amount_smudge
    
print(sum_pattern_notes)