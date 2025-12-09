from math import prod


def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5


class Circuit:
    def __init__(self, junctions, id):
        self.junctions = junctions
        self.id = id

    def __len__(self):
        return len(self.junctions)

    def __eq__(self, circuit):
        return self.id == circuit.id

    def includes(self, junction):
        return junction in self.junctions

    def merge_circuit(self, circuit):
        for j in circuit.junctions:
            self.junctions.add(j)


raw_input = open("./input.txt", "r").read()
lines = raw_input.split("\n")

# Part 1
circuits = []
junctions = []
junction_distances = []
for i in range(len(lines)):
    x, y, z = [int(j) for j in lines[i].split(",")]
    junction = (x, y, z)
    circuits.append(Circuit({junction}, i))
    junctions.append(junction)

for i in range(len(junctions)):
    for j in range(i + 1, len(junctions)):
        junction_distances.append(
            (junctions[i], junctions[j], distance(junctions[i], junctions[j])))

junction_distances.sort(key=lambda x: x[2])

for i in range(1000):
    closest_junctions = junction_distances[i]

    j1, j2 = None, None

    for index in range(len(circuits)):
        circuit = circuits[index]
        if circuit.includes(closest_junctions[0]):
            j1 = index
        if circuit.includes(closest_junctions[1]):
            j2 = index

    if j1 != j2:
        circuits[j1].merge_circuit(circuits[j2])
        circuits.pop(j2)

print(
    f"Part 1 Answer: {prod(sorted([len(x) for x in circuits], reverse=True)[:3])}")

# Part 2
circuits = []
junctions = []
junction_distances = []
for i in range(len(lines)):
    x, y, z = [int(j) for j in lines[i].split(",")]
    junction = (x, y, z)
    circuits.append(Circuit({junction}, i))
    junctions.append(junction)

for i in range(len(junctions)):
    for j in range(i + 1, len(junctions)):
        junction_distances.append(
            (junctions[i], junctions[j], distance(junctions[i], junctions[j])))

junction_distances.sort(key=lambda x: x[2])
i = 0

while 1:
    closest_junctions = junction_distances[i]

    j1, j2 = None, None

    for index in range(len(circuits)):
        circuit = circuits[index]
        if circuit.includes(closest_junctions[0]):
            j1 = index
        if circuit.includes(closest_junctions[1]):
            j2 = index

    if j1 != j2:
        circuits[j1].merge_circuit(circuits[j2])
        circuits.pop(j2)

    i += 1

    if len(circuits) == 1:
        print(
            f"Part 2 Answer: {closest_junctions[0][0]*closest_junctions[1][0]}")
        break
