tree_map = []
max_score = 0

'''Note: x:y = row:col'''

def score_left(x, y)->int:
    global max_score
    temp_score = 0
    # Compute score to the left
    left_half = [tree_map[y][i] for i in range(x - 1, -1, -1)]
    for i in range(len(left_half)):
        if tree_map[y][x] == left_half[i]:
            temp_score += 1
            break
        elif tree_map[y][x] > left_half[i]:
            temp_score += 1
        
    return temp_score


def score_right(x, y)->int:
    global max_score
    temp_score = 0
    # Compute score to the right
    right_half = [tree_map[y][i] for i in range(x + 1, len(tree_map[0]))]
    for i in range(len(right_half)):
        if tree_map[y][x] == right_half[i]:
            temp_score += 1
            break
        elif tree_map[y][x] > right_half[i]:
            temp_score += 1

    return temp_score

def score_top(x, y)->int:
    global max_score
    temp_score = 0
    # Compute score to the top
    top_half = [tree_map[i][x] for i in range(y - 1, -1, -1)]
    for i in range(len(top_half)):
        if tree_map[y][x] == top_half[i]:
            temp_score += 1
            break
        elif tree_map[y][x] > top_half[i]:
            temp_score += 1

    return temp_score

def score_bot(x, y)->int:
    global max_score
    temp_score = 0
    # Compute score to the bottom
    bot_half = [tree_map[i][x] for i in range(y + 1, len(tree_map))]
    for i in range(len(bot_half)):
        if tree_map[y][x] == bot_half[i]:
            temp_score += 1
            break
        elif tree_map[y][x] > bot_half[i]:
            temp_score += 1
    return temp_score

def get_score(x, y):
    global max_score
    # Compute product of all scenic scores and assign to max_score
    max_score = max((score_left(x, y) * score_right(x, y) \
                     * score_top(x, y) * score_bot(x, y)), max_score)



if __name__ == "__main__":

    with open ("input.txt", "r") as file:
        # Create a 2D list for the tree map
        for line in file:
            row = [int(tree) for tree in line.strip()]
            tree_map.append(row)

        # Iterate over every tree
        for x in range(len(tree_map)):
            for y in range(len(tree_map[0])):
                get_score(x, y)

    print(max_score)