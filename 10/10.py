input = [i.split(" ") for i in open("10/input.txt","r").read().splitlines()]

X, cycle = 1, 1
log = []

def check_increment_cycle():
    global cycle, log
    log.append([cycle,X])
    cycle += 1        

for line in input:    
    if line[0] == "noop":
        check_increment_cycle()
        continue
    if line[0] == "addx":
        check_increment_cycle()
        check_increment_cycle()
        X += int(line[1])
        continue    

print(sum([a*b for a,b in log if a in range(20,221,40)]))

for n in range(0,201,40):
    pixels = [0]*40
    for cycle,X in log[n:n+40]:
        sprite_positions = [X-1,X,X+1]
        if (cycle-1-n) in sprite_positions:
            pixels[cycle-1-n] = 1
    print("".join(["█" if pixel else " " for pixel in pixels]))