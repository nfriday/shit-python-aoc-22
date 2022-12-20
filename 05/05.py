import re

data, raw_moves = open("05/input.txt","r").read().split("\n\n")

raw_grid = [i[1:len(i):4] for i in data.splitlines()[:-1]]

def get_grid():
    grid = []
    for i in range(len(raw_grid[0])):
        grid.append(list(reversed([j[i] for j in raw_grid if j[i] != " "])))
    return grid

grid = get_grid()

moves = [[int(j) for j in re.search("^move (\d+) from (\d+) to (\d+)$",i).groups()] for i in raw_moves.splitlines()]

for count, source, dest in moves:
    for _ in range(count):
        grid[dest-1].append(grid[source-1].pop())

message = "".join([i[-1] for i in grid])
print(message)

# part 2

grid = get_grid()

for count, source, dest in moves:
    shift = grid[source-1][-count:]
    grid[source-1] = grid[source-1][:-count]
    grid[dest-1].extend(shift)

message = "".join([i[-1] for i in grid])
print(message)