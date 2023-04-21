# Use linear search for max_sum
max_sum = 0
temp_sum = 0

# Open input file
with open("day_1.txt", "r") as file:
    for line in file:
        # If line is not a whitespace, add to temp_sum; if not, compare max with max_sum
        if line.strip():
            temp_sum += int(line)
        else:
            max_sum = max(max_sum, temp_sum)
            temp_sum = 0

# Compare max sum for remaining numbers
max_sum = max(max_sum, temp_sum)

print(max_sum)