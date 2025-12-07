raw_input = open("./input.txt", "r").read().split("\n")

grid = [list("."*(len(raw_input[0]) + 2)),
        *[list(f".{x}.") for x in raw_input],
        list("."*(len(raw_input[0]) + 2))]

total_accessible = 0

# Part 1
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] == ".":
            continue

        adj = 0

        if grid[y - 1][x - 1] == "@":
            adj += 1
        if grid[y - 1][x] == "@":
            adj += 1
        if grid[y - 1][x + 1] == "@":
            adj += 1

        if grid[y][x - 1] == "@":
            adj += 1
        if grid[y][x + 1] == "@":
            adj += 1

        if grid[y + 1][x - 1] == "@":
            adj += 1
        if grid[y + 1][x] == "@":
            adj += 1
        if grid[y + 1][x + 1] == "@":
            adj += 1

        if adj < 4:
            total_accessible += 1

print(f"Part 1 Answer: {total_accessible}")

# Part 2
halt = False
total_accessible = 0
while not halt:
    halt = True

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == ".":
                continue

            adj = 0

            if grid[y - 1][x - 1] == "@":
                adj += 1
            if grid[y - 1][x] == "@":
                adj += 1
            if grid[y - 1][x + 1] == "@":
                adj += 1

            if grid[y][x - 1] == "@":
                adj += 1
            if grid[y][x + 1] == "@":
                adj += 1

            if grid[y + 1][x - 1] == "@":
                adj += 1
            if grid[y + 1][x] == "@":
                adj += 1
            if grid[y + 1][x + 1] == "@":
                adj += 1

            if adj < 4:
                total_accessible += 1
                grid[y][x] = "."
                halt = False

print(f"Part 2 Answer: {total_accessible}")
