raw_input = open("./input.txt", "r").read()

id_ranges = [list(map(int, x.split("-"))) for x in raw_input.split(",")]

# Part 1
total_invalids = 0

for start, end in id_ranges:
    for i in range(start, end + 1):
        identifier = str(i)
        first_half = identifier[:int(len(identifier) // 2)]
        second_half = identifier[int(len(identifier) // 2):]
        if first_half == second_half:
            total_invalids += i

print(f"Part 1 Answer: {total_invalids}")

# Part 2
total_invalids = 0

for start, end in id_ranges:
    for i in range(start, end + 1):
        identifier = str(i)
        ending_len = int(len(identifier) // 2)
        for length in range(1, ending_len + 1):
            temp_identifier = identifier
            partitions = set()

            while len(temp_identifier):
                partitions.add(temp_identifier[:length])
                temp_identifier = temp_identifier[length:]

            if len(partitions) == 1:
                total_invalids += i
                break

print(f"Part 2 Answer: {total_invalids}")
