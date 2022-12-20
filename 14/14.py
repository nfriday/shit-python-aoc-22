class Cave:

    def __init__(self,*instructions,entry_point,floor=False):
        flat = [item for sublist in instructions for item in sublist]        

        self.max_row = max([row for _,row in flat])
        if floor: self.max_row += 2

        self.min_col = min([col for col,_ in flat])
        self.max_col = max([col for col,_ in flat])

        if floor:
            self.min_col = self.min_col - self.max_row
            self.max_col = self.max_col + self.max_row

        self.entry_point = entry_point - self.min_col

        width = self.max_col - self.min_col + 1
        self.grid = [[0] * width for i in range(self.max_row+1)]

        for instruction in instructions:
            for i, point in enumerate(instruction[:-1]):
                col1,row1 = point
                col2,row2 = instruction[i+1]
                if col1 == col2:
                    if row1 > row2: row1, row2 = row2, row1
                    for row in range(row1,row2+1): self.grid[row][col1-self.min_col] = 1
                if row1 == row2:
                    if col1 > col2: col1, col2 = col2, col1
                    for col in range(col1-self.min_col,col2-self.min_col+1): self.grid[row1][col] = 1

        if floor:
            for col in range(len(self.grid[0])):
                self.grid[self.max_row][col] = 1

    def __str__(self):
        rows = []
        chars = {0: '.', 1: "#", 2: 'o'}
        for row in self.grid: rows.append("".join([chars[i] for i in row]))
        return "\n".join(rows)

    def drop_sand(self):
        row, col = 0, self.entry_point

        if self.grid[row][col] != 0:
            return False

        try:
            while True:
                if self.grid[row+1][col] == 0:
                    row += 1
                    continue
                if self.grid[row+1][col-1] == 0:
                    row +=1
                    col -=1
                    continue
                if self.grid[row+1][col+1] == 0:
                    row +=1
                    col +=1
                    continue
                break
        except:
            return False

        self.grid[row][col] = 2
        return True
        
input = [[[int(j) for j in i.split(",")] for i in line] for line in [line.split(" -> ") for line in open("14/input.txt").read().splitlines()]]

cave = Cave(*input,entry_point=500)

count = 0
while cave.drop_sand():
    count += 1
print(count)

count = 0
cave2 = Cave(*input,entry_point=500,floor=True)
while cave2.drop_sand():
    count += 1
print(count)


