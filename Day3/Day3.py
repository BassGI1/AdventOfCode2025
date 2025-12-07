def decrement(num):
    return str(int(num) - 1)


def digits_to_int(digits):
    return int(digits[0])*10 + int(digits[1])


raw_input = open("./input.txt", "r").read()

banks = raw_input.split("\n")
total_joltage = 0

# Part 1
for bank in banks:
    joltage_digits = ["9", "9"]
    while 1:
        dig_one_index = bank.find(joltage_digits[0])

        if dig_one_index == -1 or dig_one_index == len(bank):
            joltage_digits[0] = decrement(joltage_digits[0])
            joltage_digits[1] = "9"
            continue

        dig_two_index = bank.find(joltage_digits[1], dig_one_index + 1)

        if dig_two_index == -1:
            if joltage_digits[1] == "1":
                joltage_digits[0] = decrement(joltage_digits[0])
                joltage_digits[1] = "9"
            else:
                joltage_digits[1] = decrement(joltage_digits[1])
            continue

        total_joltage += digits_to_int(joltage_digits)
        break

print(f"Part 1 Answer: {total_joltage}")

# Part 2
total_joltage = 0
for bank in banks:
    joltage = "999999999999"
    remaining_batteries = bank
    i = 0

    while 1:
        if i > 11:
            total_joltage += int(joltage)
            break

        digit = joltage[i]
        index = remaining_batteries.find(digit)

        if index == -1:
            prefix = decrement(joltage[:i + 1])
            filler_len = len(joltage[i + 1:])

            while "0" in prefix:
                prefix = decrement(prefix)
                filler_len += 1
                prefix = prefix[:-1]

            joltage = prefix + filler_len*"9"
            i = 0
            remaining_batteries = bank
            continue

        i += 1
        remaining_batteries = remaining_batteries[index + 1:]

print(f"Part 2 Answer: {total_joltage}")
