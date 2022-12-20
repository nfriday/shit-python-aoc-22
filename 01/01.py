input = open("01/input.txt","r").read().split("\n\n")

totals = [sum([int(j) for j in i.splitlines()]) for i in input]
print(max(totals))

totals.sort()
print(sum(totals[-3:]))