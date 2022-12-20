import copy

def get_grid_val(x):
    if x == "S": return ord("a")
    if x == "E": return ord("z")
    return ord(x)

grid = [[[i,get_grid_val(i),99999,None] for i in list(line)] for line in open("12/input.txt","r").read().splitlines()]

def get_valid_adjacent(grid,row,col):
    neighbours = [[r,c] for r,c in [[row+1,col], [row-1,col], [row,col+1], [row,col-1]] if r >=0 and c >=0 and r<len(grid) and c<len(grid[0])]
    valid_neighbours = [[r,c] for r,c in neighbours if grid[r][c][1] <= grid[row][col][1] + 1]
    return valid_neighbours

def find_coords(grid,x):
    coords = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c][0] == x: coords.append([r,c])
    return coords

def solve(grid,start,end,valid_neighbour_function,return_solved_grid=False):
    grid = copy.deepcopy(grid)
    start_row, start_col = start
    grid[start_row][start_col][2] = 0

    unvisited = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            unvisited.append([r,c])

    while unvisited:
        unvisited.sort(key=lambda i: grid[i[0]][i[1]][2])
        current_row, current_col = unvisited.pop(0)
        valid_neighbours = [i for i in valid_neighbour_function(grid,current_row,current_col) if i in unvisited]
        current_distance_from_start = grid[current_row][current_col][2]
        for neighbour_row, neighbour_col in valid_neighbours:
            new_distance = current_distance_from_start + 1
            known_distance = grid[neighbour_row][neighbour_col][2]
            if new_distance < known_distance:
                grid[neighbour_row][neighbour_col][2] = new_distance
                grid[neighbour_row][neighbour_col][3] = [current_row, current_col]

    if return_solved_grid: return grid

    end_row, end_col = end
    return grid[end_row][end_col][2]

# part 1
start = find_coords(grid,"S")[0]
end = find_coords(grid,"E")[0]
print(solve(grid,start,end,get_valid_adjacent))

# part 2
def get_valid_adjacent_reversed(grid,row,col):
    neighbours = [[r,c] for r,c in [[row+1,col], [row-1,col], [row,col+1], [row,col-1]] if r >=0 and c >=0 and r<len(grid) and c<len(grid[0])]
    valid_neighbours = [[r,c] for r,c in neighbours if grid[r][c][1] >= grid[row][col][1] - 1]
    return valid_neighbours

reverse_paths = []
solved_reverse_grid = solve(grid,end,start,get_valid_adjacent_reversed,True)
for r in range(len(solved_reverse_grid)):
    for c in range(len(solved_reverse_grid[0])):
        if solved_reverse_grid[r][c][0] == "a": reverse_paths.append(solved_reverse_grid[r][c][2])
print(min(reverse_paths))