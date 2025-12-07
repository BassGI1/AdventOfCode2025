def print_grid(g):
    n = ""
    for line in g:
        temp = ""
        for a in line:
            temp = f"{temp} {a if a != 0 else "."}"
        n = f"{n}\n{temp}"
    print(n)


raw_input = open("./input.txt", "r").read()
grid = [list(l) for l in raw_input.split("\n")]

# Part 1
active_tachyons = set()

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            active_tachyons.add((x, y))
            break

    if len(active_tachyons):
        break

num_splits = 0

while len(active_tachyons):
    new_tachyons = set()
    for x, y in active_tachyons:
        if y == len(grid) - 1:
            continue

        if grid[y + 1][x] == "^":
            grid[y + 1][x - 1] = "|"
            grid[y + 1][x + 1] = "|"
            new_tachyons.add((x + 1, y + 1))
            new_tachyons.add((x - 1, y + 1))
            num_splits += 1
        else:
            grid[y + 1][x] = "|"
            new_tachyons.add((x, y + 1))
    active_tachyons = new_tachyons

print(f"Part 1 Answer: {num_splits}")


# Part 2
active_tachyons = set()
grid = [list(l) for l in raw_input.split("\n")]

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "^":
            continue
        if grid[y][x] == "S":
            active_tachyons.add((x, y))
            grid[y][x] = 1
        else:
            grid[y][x] = 0

while len(active_tachyons):
    new_tachyons = set()
    for x, y in active_tachyons:
        if y == len(grid) - 1:
            continue

        if grid[y + 1][x] == "^":
            grid[y + 1][x - 1] += grid[y][x]
            grid[y + 1][x + 1] += grid[y][x]
            new_tachyons.add((x + 1, y + 1))
            new_tachyons.add((x - 1, y + 1))

        else:
            grid[y + 1][x] += grid[y][x]
            new_tachyons.add((x, y + 1))

    active_tachyons = new_tachyons

print(f"Part 2 Answer: {sum(grid[-1])}")
