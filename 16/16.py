import re

input = [re.search("^Valve (..) has flow rate=(\d+); tunnels* leads* to valves* (.*)$",line).groups() for line in open("16/input.txt").read().splitlines()]
nodes = { name: {'pressure': int(pressure), 'connections': connections.split(", ")} for name, pressure, connections in input}

print(nodes)