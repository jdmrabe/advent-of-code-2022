visited_pos = [[0,0]]
head_pos = [0,0] # Set as origin; [x,y]
tail_pos = [0,0]

def move_head(line):
    global head_pos
    h_dir = line[0]
    h_mov = int(line[1])
    for i in range(h_mov):
        if h_dir == "U":
            head_pos[1] += 1
        elif h_dir == "D":
            head_pos[1] -= 1
        elif h_dir == "L":
            head_pos[0] -= 1
        elif h_dir == "R":
            head_pos[0] += 1
        move_tail()

def move_tail():
    global tail_pos
    # Check if not same row or caolumn; order to move diagonally
    if (tail_pos[0] != head_pos[0] or tail_pos[1] != head_pos[1]) and \
        (abs(head_pos[0] - tail_pos[0]) >= 2 or abs(head_pos[1] - tail_pos[1]) >= 2):
        if head_pos[0] > tail_pos[0]:
            tail_pos[0] += 1 
        elif head_pos[0] < tail_pos[0]:
            tail_pos[0] -= 1
        if head_pos[1] > tail_pos[1]:
            tail_pos[1] += 1 
        elif head_pos[1] < tail_pos[1]:
            tail_pos[1] -= 1
        visit_pos()
        return
    # Check if head is 2 steps ahead
    elif abs(head_pos[0] - tail_pos[0]) >= 2 or abs(head_pos[1] - tail_pos[1]) >= 2:
        tail_pos[0] += 1 if tail_pos[0] > head_pos[0] else - 1
        tail_pos[1] += 1 if head_pos[1] > tail_pos[1] else - 1
        visit_pos()
        return

def visit_pos():
    global visited_pos
    # Check if current position is added, if not, add
    if tail_pos not in visited_pos:
        visited_pos.append(list(tail_pos))
    

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        for lines in file:
            line = lines.strip().split()
            move_head(line) 
            
    print(len(visited_pos))