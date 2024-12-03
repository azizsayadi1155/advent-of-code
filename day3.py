# PART 1
import re

total_sum = 0

with open("input.txt", 'r') as f:
    for line in f:
        matches = re.findall(r"mul\((\d+),(\d+)\)", line)

        for match in matches:
            x, y = map(int, match)
            total_sum += x * y

print(total_sum)


# PART 2

total_sum = 0
enabled = True

with open("input.txt", 'r') as f:
    for line in f:
        instructions = re.split(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", line)

        for instruction in instructions:
            if instruction == "do()":
                enabled = True
            elif instruction == "don't()":
                enabled = False
            elif instruction.startswith("mul(") and enabled:
                match = re.match(r"mul\((\d+),(\d+)\)", instruction)
                if match:
                    x, y = map(int, match.groups())
                    total_sum += x * y

print(total_sum)
