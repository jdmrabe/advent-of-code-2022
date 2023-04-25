visited = [[0,0]]
# Assign origin coordinates [0,0] to all knots of rope
rope = [[0,0] for i in range(10)] 

def move_rope(line):
    global rope
    dir = line[0]
    mov = int(line[1])
    for i in range(mov):
        if dir == "U":
            rope[0][1] += 1
        elif dir == "D":
            rope[0][1] -= 1
        elif dir == "L":
            rope[0][0] -= 1
        elif dir == "R":
            rope[0][0] += 1

        # Simulate movement of remaining 9 knots, curr knot is relative prev knot at rope(i + 1)
        for i in range(9):
            prev = rope[i]
            curr = rope[i + 1]
            # Check if not same row or column; order to move diagonally
            if (curr[0] != prev[0] or curr[1] != prev[1]) and \
                (abs(prev[0] - curr[0]) >= 2 or abs(prev[1] - curr[1]) >= 2):
                if prev[0] > curr[0]:
                    curr[0] += 1 
                elif prev[0] < curr[0]:
                    curr[0] -= 1
                if prev[1] > curr[1]:
                    curr[1] += 1 
                elif prev[1] < curr[1]:
                    curr[1] -= 1

            # Check if prev knot is 2 steps ahead
            elif abs(prev[0] - curr[0]) >= 2 or abs(prev[1] - curr[1]) >= 2:
                curr[0] += 1 if curr[0] > prev[0] else - 1
                curr[1] += 1 if prev[1] > curr[1] else - 1
                
        # Check if current position is added, if not, add
        if rope[-1] not in visited:
            visited.append(list(rope[-1]))
    

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        for lines in file:
            line = lines.strip().split()
            move_rope(line) 
            
    print(len(visited))