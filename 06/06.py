input = list(open("06/input.txt","r").read())

def get_marker(x) -> int:
    for i in range(x,len(input)):
        last = input[i-x:i]
        if len(last) == len(set(last)):
            break
    return i 

print(get_marker(4))

print(get_marker(14))
