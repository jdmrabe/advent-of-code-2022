# Open input file
with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        r1 = r2 = 0
        # Separate assignment pairs by lists
        assigned = line.strip().split(',')
        for rooms in assigned:
            # Separate assigned room ranges per person by list
            rooms = rooms.strip().split('-')
            if r1 == 0 and r2 == 0: # If pair 1 has not been declared, assign:
                r1 = int(rooms[0])  # Lower limit of pair 1
                r2 = int(rooms[1])  # Upper limit of pair 1
            else: # Compare range of the pair
                if (r1 <= int(rooms[0]) and r2 >= int(rooms[1])) or (r1 >= int(rooms[0]) and r2 <= int(rooms[1])) or (r1 >= int(rooms[0]) and r1 <= int(rooms[1])) or (r2 >= int(rooms[0]) and r2 <= int(rooms[1])):
                    sum += 1

print(sum)