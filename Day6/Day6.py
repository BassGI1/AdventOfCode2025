from re import findall

# this might be the worst code ive ever written in my life


def format_line_p1(line):
    pattern = r"[0-9]+"
    matches = findall(pattern, line)
    return [int(x) for x in matches]


raw_input = open("./input.txt", "r").read()
lines = raw_input.split("\n")

# Part 1
operations = lines[-1].replace(" ", "")
lines = lines[:-1]

for i in range(len(lines)):
    lines[i] = format_line_p1(lines[i])

ans_list = [0 if op == "+" else 1 for op in operations]
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if operations[x] == "*":
            ans_list[x] *= lines[y][x]
        else:
            ans_list[x] += lines[y][x]

print(f"Part 1 Answer: {sum(ans_list)}")


# Part 2
lines = raw_input.split("\n")

operations = lines[-1]
lines = lines[:-1]
problem_indices = []

for i in range(len(operations)):
    if operations[i] != " ":
        problem_indices.append(i)

for i in range(len(problem_indices) - 1):
    problem_indices[i] = (problem_indices[i], problem_indices[i + 1] - 1)
problem_indices[-1] = (problem_indices[-1], len(operations))

total = 0

for i in range(len(problem_indices)):
    start, end = problem_indices[i]
    operation = operations[start]
    nums_strs = []

    for line in lines:
        nums_strs.append(line[start: end])

    nums = list(" "*len(nums_strs))
    for index in range(len(nums_strs[0])):
        for num in nums_strs:
            nums[index] = f"{nums[index]}{num[index]}"

    nums = list(filter(lambda x: x != " ", nums))
    nums = [int(n.replace(" ", "")) for n in nums]
    s = 0 if operation == "+" else 1

    for num in nums:
        if operation == "+":
            s += num
        else:
            s *= num

    total += s

print(f"Part 2 Answer: {total}")
