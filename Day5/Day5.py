raw_input = open("./input.txt", "r").read()

fresh_ranges, ingredient_ids = raw_input.split("\n\n")
ingredient_ids = [int(i) for i in ingredient_ids.split("\n")]
fresh_ranges = sorted([(int(start), int(end)) for start, end in [
    r.split("-") for r in fresh_ranges.split("\n")]], key=lambda x: x[0])

halt = False
i = 1

while not halt:
    halt = True

    while i < len(fresh_ranges):
        start, end = fresh_ranges[i]
        prev_start, prev_end = fresh_ranges[i - 1]
        if start <= prev_end:
            fresh_ranges[i] = (min(prev_start, start), max(prev_end, end))
            fresh_ranges.pop(i - 1)
            i = 1
            halt = False
            break
        i += 1

# Part 1
range_index = 0
num_fresh = 0

for ingredient in ingredient_ids:
    for start, end in fresh_ranges:
        if ingredient in range(start, end + 1):
            num_fresh += 1
            break

print(f"Part 1 Answer: {num_fresh}")

# Part 2
num_fresh = 0
for start, end in fresh_ranges:
    num_fresh += end - start + 1

print(f"Part 2 Answer: {num_fresh}")