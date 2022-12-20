import numpy as np
from datetime import datetime

input = [[line[0],int(line[2:])] for line in open("09/input.txt","r").read().splitlines()]

transforms = {
    "R": np.array([0,1]),
    "L": np.array([0,-1]),
    "U": np.array([-1,0]),
    "D": np.array([1,0])
}

def step(rope,direction):
    rope[0] = rope[0] + transforms[direction]
    for i in range(len(rope)-1):            
        tail_distance = rope[i] - rope[i+1]
        if max(abs(tail_distance)) <= 1: return
        rope[i+1] = rope[i+1] + [i//abs(i) if i else 0 for i in tail_distance]

def solve(rope_length,input) -> int:
    rope = [np.array(i) for i in [[0,0]]*rope_length]
    visited = []
    for direction, length in input:
        for _ in range(length):
            step(rope,direction)
            tail_list = list(rope[-1])
            if tail_list not in visited: visited.append(tail_list)
    return len(visited)

print(solve(2,input))

print(solve(10,input))
