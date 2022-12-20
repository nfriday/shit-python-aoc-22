import re
import functools

input = [[eval(j) for j in i.splitlines()] for i in open("13/input.txt").read().split("\n\n")]

def compare(a,b):
    if type(a) is int and type(b) is int:
        if a<b: return -1
        if a>b: return 1
    if type(a) is list and type(b) is list:
        for a1,b1 in zip(a,b):
            compared = compare(a1,b1)
            if compared: return compared
        if len(a)<len(b): return -1
        if len(a)>len(b): return 1        
    if type(a) is int and type(b) is list:
        compared = compare([a],b)
        if compared: return compared
    if type(a) is list and type(b) is int:
        compared = compare(a,[b])
        if compared: return compared
    return 0

print(sum([i+1 for i, val in enumerate(input) if compare(*val) == -1]))

input2 = [eval(i) for i in open("13/input.txt").read().splitlines() if len(i)]
input2.append([[2]])
input2.append([[6]])

input2.sort(key=functools.cmp_to_key(compare))

print((input2.index([[2]])+1) * (input2.index([[6]])+1))

