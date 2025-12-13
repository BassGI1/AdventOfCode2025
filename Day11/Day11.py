raw_input = open("./input.txt", "r").read()
lines = raw_input.split("\n")

wiring = {}

for line in lines:
    wire, outputs = line.split(": ")
    wiring[wire] = {o for o in outputs.split(" ")}

# Part 1
total = 0
stack = ["you"]

while len(stack):
    wire = stack.pop(0)
    if wire == "out":
        total += 1
        continue
    for w in wiring[wire]:
        stack.append(w)

print(f"Part 1 Answer: {total}")


# Part 2
# the following ugly behemoths of code should just be repeated calls to a function but i cba and it works

svr_to_fft = 0
to_process = [("svr", 1)]
while len(to_process):
    seen = {}

    for wire, count in to_process:
        if wire == "out" or wire == "dac":
            continue
        elif wire == "fft":
            svr_to_fft += count
            continue
        else:
            for w in wiring[wire]:
                if w not in seen:
                    seen[w] = count
                else:
                    seen[w] += count

    to_process = list(seen.items())


svr_to_dac = 0
to_process = [("svr", 1)]
while len(to_process):
    seen = {}

    for wire, count in to_process:
        if wire == "out" or wire == "fft":
            continue
        elif wire == "dac":
            svr_to_dac += count
            continue
        else:
            for w in wiring[wire]:
                if w not in seen:
                    seen[w] = count
                else:
                    seen[w] += count

    to_process = list(seen.items())


dac_to_fft = 0
to_process = [("dac", svr_to_dac)]
while len(to_process):
    seen = {}

    for wire, count in to_process:
        if wire == "out":
            continue
        elif wire == "fft":
            dac_to_fft += count
            continue
        else:
            for w in wiring[wire]:
                if w not in seen:
                    seen[w] = count
                else:
                    seen[w] += count

    to_process = list(seen.items())


fft_to_dac = 0
to_process = [("fft", svr_to_fft)]
while len(to_process):
    seen = {}

    for wire, count in to_process:
        if wire == "out":
            continue
        elif wire == "dac":
            fft_to_dac += count
            continue
        else:
            for w in wiring[wire]:
                if w not in seen:
                    seen[w] = count
                else:
                    seen[w] += count

    to_process = list(seen.items())


total = 0
to_process = [("fft", dac_to_fft)]
while len(to_process):
    seen = {}

    for wire, count in to_process:
        if wire == "out":
            total += count
            continue
        elif wire == "dac":
            continue
        else:
            for w in wiring[wire]:
                if w not in seen:
                    seen[w] = count
                else:
                    seen[w] += count

    to_process = list(seen.items())


to_process = [("dac", fft_to_dac)]
while len(to_process):
    seen = {}

    for wire, count in to_process:
        if wire == "out":
            total += count
            continue
        elif wire == "fft":
            continue
        else:
            for w in wiring[wire]:
                if w not in seen:
                    seen[w] = count
                else:
                    seen[w] += count

    to_process = list(seen.items())


print(f"Part 2 Answer: {total}")