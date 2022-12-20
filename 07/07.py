import re

input = open("07/input.txt","r").read().splitlines()

dir = ["/"]
dirsizes = {}
for line in input:

    parts = line.split(" ")

    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "..":
                dir.pop()
            elif parts[2] == "/":
                dir = ["/"]
            else:
                dir.append(parts[2])
        continue

    if parts[0] == "dir":
        continue

    size = int(parts[0])

    for i in range(len(dir)):
        strdir = "/".join(dir[0:i+1])
        if strdir not in dirsizes:
            dirsizes[strdir] = 0
        dirsizes[strdir] += size

print(sum([i for i in dirsizes.values() if i <= 100000]))

total_diskspace = 70000000
target_freespace = 30000000
available_diskspace = total_diskspace - dirsizes["/"]
needed_diskspace = target_freespace - available_diskspace

print(min([i for i in dirsizes.values() if i>=needed_diskspace]))