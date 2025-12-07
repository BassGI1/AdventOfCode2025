def convert_rotation(rot):
    direction = rot[0]
    rotation = int(rot[1:])
    return rotation if direction == "R" else rotation*-1


raw_input = open("./input.txt", "r").read()
rotations = list(map(convert_rotation, raw_input.split("\n")))

rotation_val = 50
total_zeroes = 0

# Part 1
for rotation in rotations:
    rotation_val = (rotation_val + 100 + rotation) % 100
    if rotation_val == 0:
        total_zeroes += 1

print(f"Part 1 Answer: {total_zeroes}")

# Part 2
rotation_val = 50
total_zeroes = 0

for rotation in rotations:
    if rotation < 0:
        for _ in range(1, abs(rotation) + 1):
            rotation_val = (rotation_val + 99) % 100
            if rotation_val == 0:
                total_zeroes += 1
    else:
        for _ in range(1, rotation + 1):
            rotation_val = (rotation_val + 101) % 100
            if rotation_val == 0:
                total_zeroes += 1

print(f"Part 2 Answer: {total_zeroes}")
