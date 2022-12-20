import re

input = open("04/input.txt","r").read().splitlines()
data = [[int(j) for j in re.search("(\d+)-(\d+),(\d+)-(\d+)",i).groups()] for i in input]

overlaps = [i for i in data if (i[0]<=i[2] and i[1]>=i[3]) or (i[0]>=i[2] and i[1]<=i[3])]
print(len(overlaps))

overlaps2 = [i for i in data if (i[2]<=i[0]<=i[3]) or (i[0]<=i[2]<=i[1]) or (i[2]<=i[1]<=i[3]) or (i[0]<=i[3]<=i[1])]
print(len(overlaps2))