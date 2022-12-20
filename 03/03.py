input = open("03/input.txt","r").read().splitlines()

input_lists = [list(line) for line in input]
sacks = [(i[:len(i)//2],i[len(i)//2:]) for i in input_lists]

def priority(char):
    x = ord(char)
    if x >= 97:
        return x - 96
    return x - 38

sum = 0
for sack in sacks:
    duplicate = [i for i in sack[0] if i in sack[1]][0]
    sum += priority(duplicate)

print(sum)

# part 2

groups = [[list(j) for j in input[i:i+3]] for i in range(0,len(input),3)]

sum2 = 0
for group in groups:
    duplicate = [i for i in group[0] if i in group[1] and i in group[2]][0]
    sum2 += priority(duplicate)

print(sum2)