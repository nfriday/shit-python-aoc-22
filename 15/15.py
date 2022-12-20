import re

def md(a,b): return abs(a[0]-b[0]) + abs(a[1]-b[1])

def merge_ranges(ranges):
    ranges.sort(key=lambda i: i[0])
    merged = [ranges[0]]

    for i in range(1,len(ranges)):
        low1,high1 = merged.pop()
        low2,high2 = ranges[i]
        if low2 >= low1 and low2 <= high1:
            merged.append([low1,max(high1,high2)])
        else:
            merged.append([low1,high1])
            merged.append([low2,high2])
    return merged

class Grid:
    def __init__(self,*input):
        self.data = [{"sensor": (sx,sy), "beacon": (bx,by), "distance": md((sx,sy),(bx,by))} for sx,sy,bx,by in input]

    def impossible_x_on_y_ranges(self,y):
        nearer_sensors =  [i for i in self.data if abs(i["sensor"][1]-y) < i["distance"]]
        impossible = []
        for n in self.data:
            distance_to_y = abs(n["sensor"][1]-y)
            closer_by = n["distance"] - distance_to_y
            if closer_by <= 0: continue
            impossible.append([n["sensor"][0]-closer_by,n["sensor"][0]+closer_by])
        impossible_ranges = merge_ranges(impossible)
        return impossible_ranges

    def impossible_x_on_y_count(self,y):
        impossible_ranges = self.impossible_x_on_y_ranges(y)
        beacon_x_on_y = set([i["beacon"][0] for i in self.data if i["beacon"][1]==y])
        beacon_x_on_y_in_impossible_ranges = 0
        for x in beacon_x_on_y:
            if [r for r in impossible_ranges if x >= r[0] and x <= r[1]]:
                beacon_x_on_y_in_impossible_ranges -= 1
        return sum([b-a+1 for a,b in impossible_ranges]) + beacon_x_on_y_in_impossible_ranges

    def find_distress_beacon(self,minx,miny,maxx,maxy):
        for y in range(miny,maxy+1):
            impossible_ranges = self.impossible_x_on_y_ranges(y)
            for minr,maxr in impossible_ranges:
                if maxr<maxx: return [maxr+1,y]
                if minr>minx: return [minr-1,y]

    def tuning_frequency(self,x,y):
        return 4000000*x+y

input = [[int(i) for i in re.search("Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)",i).groups()] for i in open("15/input.txt","r").read().splitlines()]

grid = Grid(*input)

impossible = print(grid.impossible_x_on_y_count(10))

print(grid.tuning_frequency(*grid.find_distress_beacon(0,0,4000000,4000000)))