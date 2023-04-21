# Create a list for sums
sums = []
temp_sum = 0

# Open input file
with open("input.txt", "r") as file:
    for line in file:
        # If line is not a whitespace, add to temp_sum; if not, append temp_sum to list
        if line.strip():
            temp_sum += int(line)
        else:
            sums.append(temp_sum)
            temp_sum = 0
    sums.append(temp_sum)
# Sort sums in descending order
sums.sort(reverse=True)
# Sum the 3 highest sums
top3_sum = sum(sums[:3])

print(top3_sum)