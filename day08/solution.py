tree_map = []
trees_visible = 0
    
def on_edge(x, y)->bool:
    """
    Check if tree is at the edge of the tree map
    """
    global trees_visible
    edge_value = [0, (len(tree_map[0]) - 1)]
    if x in edge_value or y in edge_value:
        return True
    else:
        return False

def visible_x(x, y)->bool:
    global trees_visible
    """
    Check if any of the sides are all shorter; visible
    """
    left_half = [tree_map[i][y] for i in range(0, x)]
    if left_half and max(left_half) < tree_map[x][y]:
            return True
    right_half = [tree_map[i][y] for i in range(x + 1, len(tree_map))]
    if right_half and max(right_half) < tree_map[x][y]:
            return True
    #Neither half has all shorter trees; not visible
    return False
    

def visible_y(x, y)->bool:
    global trees_visible
    """
    Check if any of the sides are all shorter; visible
    """
    top_half = tree_map[x][:y]
    if top_half and max(top_half) < tree_map[x][y]:
            return True
    bottom_half = tree_map[x][y+1:]
    if bottom_half and max(bottom_half) < tree_map[x][y]:
            return True
    # Neither half has all shorter trees; not visible
    return False

if __name__ == "__main__":

    with open ("input.txt", "r") as file:
        # Create a 2D list for the tree map
        for line in file:
            row = [int(tree) for tree in line.strip()]
            tree_map.append(row)

        # Iterate over every tree
        for x in range(len(tree_map)):
            for y in range(len(tree_map[0])):
                if on_edge(x, y):
                    trees_visible += 1
                elif visible_x(x, y) or visible_y(x, y):
                    trees_visible += 1

    print(trees_visible)
