input = open("02/input.txt","r").read().splitlines()

data = [i.split(" ") for i in input]

shapes = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3 }
win = {2:1, 3:2, 1:3}

def score(me,them):
    if me == them:
        return 3 + me
    if win[me] == them:
        return 6 + me
    return 0 + me

scores = [score(shapes[me],shapes[them]) for them, me in data]

print(sum(scores))

# part 2
loss = {v:k for k,v in win.items()}

def score2(them,token):
    if token == "Y":
        return them + 3
    if token == "X":
        return win[them] + 0
    if token == "Z":
        return loss[them] + 6

scores2 = [score2(shapes[them],token) for them, token in data]

print(sum(scores2))