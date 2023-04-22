# Initialize dict of lists
supply_stack = {
1: ['B', 'W', 'N'],
2: ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
3: ['Q', 'H', 'Z', 'W', 'R'],
4: ['W', 'D', 'V', 'J', 'Z', 'R'],
5: ['S', 'H', 'M', 'B'],
6: ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
7: ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
8: ['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
9: ['Z', 'W', 'M', 'S', 'C', 'D', 'J'],
}
temp_stack = []

# Pop and append according to input file
def run(arr: list):
    for crates in range(arr[0]):
        current_crate = supply_stack[arr[1]].pop()
        temp_stack.append(current_crate)
    for crates in range(arr[0]):
        current_crate = temp_stack.pop()
        supply_stack[arr[2]].append(current_crate)

# Iterate through input instructions
with open("input.txt", "r") as f:
    lines = f.readlines()[10:]
    for line in lines:
        parts = line.strip().split()
        crate_amount, from_stack, to_stack = map(int, parts[1::2])
        order = [crate_amount, from_stack, to_stack]
        run(order)

# Print top most crates of each stack
for stack in supply_stack:
    print(f"{supply_stack[stack][-1]}", end="")