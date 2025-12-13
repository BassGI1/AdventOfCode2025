from time import time

def parse_light_diagram(s):
    return [l == "#" for l in list(s)[1:-1]]


def parse_button(s):
    return [int(b) for b in list(s[1:-1].split(","))]


def parse_joltage(s):
    return [int(j) for j in s[1:-1].split(",")]


def compare_lists(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def build_combinations(sample_space, n):
    if n == 1:
        return {tuple([c]) for c in sample_space}

    combinations = build_combinations(sample_space, n - 1)
    copy = combinations.copy()

    for c in combinations:
        for s in sample_space:
            if s not in c:
                copy.add(tuple(set((*c, s))))

    return copy


raw_input = open("./input.txt", "r").read()

lines = raw_input.split("\n")
machines = []

for line in lines:
    split = line.split(" ")
    lights = parse_light_diagram(split[0])
    buttons = list(map(parse_button, split[1:-1]))
    joltages = parse_joltage(split[-1])
    machines.append((lights, buttons, joltages))

# # Part 1
# total = 0
# for target_lights, buttons, _ in machines:
#     combinations = sorted(build_combinations(
#         [i for i in range(len(buttons))], len(buttons)), key=lambda x: len(x))

#     for combination in combinations:
#         curr_lights = [False for _ in range(len(target_lights))]
#         actions = [buttons[i] for i in list(combination)]

#         for action in actions:
#             for l in action:
#                 curr_lights[l] = not curr_lights[l]

#         if compare_lists(curr_lights, target_lights):
#             total += len(actions)
#             break

# print(f"Part 1 Answer: {total}")

#  1 -> correct
#  0 -> not correct, still possible
# -1 -> not correct


def test_joltages(curr, target):
    at_max = False
    correctness = 1
    for i in range(len(curr)):
        if curr[i] == target[i]:
            at_max = True
        if (curr[i] != target[i] and at_max) or (curr[i] > target[i]):
            return -1
        if curr[i] != target[i]:
            correctness = 0
    return correctness


def largest_diff(curr, target):
    diff = 0
    diff_index = -1
    for i in range(len(curr)):
        if target[i] - curr[i] > diff:
            diff = target[i] - curr[i]
            diff_index = i
    return diff_index


def test_combination_p2(buttons, current, target, num_presses, val_found, seen):
    seen.add(tuple(current))

    correctness = test_joltages(current, target)
    if correctness == 1:
        val_found[0] = num_presses
        return
    elif correctness == -1:
        return

    largest_diff_index = largest_diff(current, target)
    buttons = sorted(buttons, key=lambda x: len(x)*-1 + 10 if largest_diff_index in x else len(x)*-1, reverse=True)

    for button in buttons:
        if val_found[0] == 0:
            copy = current.copy()
            for b in button:
                copy[b] += 1
            if tuple(copy) not in seen:
                test_combination_p2(buttons, copy, target,
                                    num_presses + 1, val_found, seen)

timer = time()
for _, buttons, joltages in machines:
    val = [0]
    b = sorted([set(x) for x in buttons], key=lambda x: len(x), reverse=True)
    test_combination_p2(b, [0 for _ in range(
        len(joltages))], joltages, 0, val, set())
    temp = time()
    print(val[0], int((temp - timer) // 60))
    timer = temp
    
