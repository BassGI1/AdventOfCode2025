from shapely.geometry import Polygon


def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


raw_input = open("./input.txt", "r").read()

red_tiles = [list(map(int, r.split(","))) for r in raw_input.split("\n")]

# Part 1
max_area = 0
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        max_area = max(max_area, area(red_tiles[i], red_tiles[j]))

print(f"Part 1 Answer: {max_area}")

# Part 2
# using shapely feels like cheating

max_area = 0
p = Polygon(red_tiles)
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        min_x = min(red_tiles[i][0], red_tiles[j][0])
        max_x = max(red_tiles[i][0], red_tiles[j][0])

        min_y = min(red_tiles[i][1], red_tiles[j][1])
        max_y = max(red_tiles[i][1], red_tiles[j][1])

        rectangle = Polygon([
            (min_x, min_y),
            (max_x, min_y),
            (max_x, max_y),
            (min_x, max_y)
        ])

        if p.covers(rectangle):
            max_area = max(max_area, area(red_tiles[i], red_tiles[j]))

print(f"Part 2 Answer: {max_area}")
