import itertools

input = open("08/input.txt","r").read().splitlines()

grid = [[int(j) for j in i] for i in input]

def is_visible(x,y) -> bool:

    if (0 in [x,y]) or (x == len(grid[0])-1) or (y == len(grid)-1):
        return True

    trees_left = [grid[x][i] for i in range(y)]
    if max(trees_left) < grid[x][y]: return True

    trees_right = [grid[x][i] for i in range(y+1,len(grid[0]))]
    if max(trees_right) < grid[x][y]: return True

    trees_up = [grid[i][y] for i in range(x)]
    if max(trees_up) < grid[x][y]: return True

    trees_down = [grid[i][y] for i in range(x+1,len(grid))]
    if max(trees_down) < grid[x][y]: return True

    return False

trees = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if is_visible(x,y): trees += 1

print(trees)

def scenic_score(x,y) -> int:

    if (0 in [x,y]) or (x == len(grid[0])-1) or (y == len(grid)-1):
        return 0

    this_tree = grid[x][y]

    left_score = 0
    trees_left = [grid[x][i] for i in range(y)]
    for tree in reversed(trees_left):
        left_score += 1
        if tree >= this_tree: break        
    if left_score == 0: return 0

    right_score = 0
    trees_right = [grid[x][i] for i in range(y+1,len(grid[0]))]
    for tree in trees_right:
        right_score += 1
        if tree >= this_tree: break        
    if right_score == 0: return 0

    up_score = 0
    trees_up = [grid[i][y] for i in range(x)]
    for tree in reversed(trees_up):
        up_score += 1
        if tree >= this_tree: break        
    if up_score == 0: return 0

    down_score = 0
    trees_down = [grid[i][y] for i in range(x+1,len(grid))]
    for tree in trees_down:
        down_score += 1
        if tree >= this_tree: break        
    if down_score == 0: return 0

    return left_score * right_score * up_score * down_score

max_score = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        score = scenic_score(x,y)
        if score > max_score: max_score = score

print(max_score)