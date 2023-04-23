tree_map = []
trees_visible = 0
    
def on_edge(x, y)->bool:
    global trees_visible
    edge_value = [0, (len(tree_map[0]) - 1)]
    if x in edge_value or y in edge_value:
        return True
    else:
        return False

def visible_x(x, y)->bool:
    global trees_visible
    for i in range(len(tree_map)):
        if tree_map[x][i] >= tree_map[x][y] and i != y:
            return False
        else:
            return True

def visible_y(x, y)->bool:
    global trees_visible
    for i in range(len(tree_map[0])):
        if tree_map[i][y] >= tree_map[x][y] and i != x:
            return False
    return True

if __name__ == "__main__":

    with open ("input.txt", "r") as file:
        for line in file:
            # Create a 2D list for the tree map
            row = [int(tree) for tree in line.strip()]
            tree_map.append(row)

        for x in range(len(tree_map)):
            for y in range(len(tree_map[0])):
                if on_edge(x, y):
                    trees_visible += 1
                elif visible_x(x, y) or visible_y(x, y):
                    trees_visible += 1

    print(trees_visible)

