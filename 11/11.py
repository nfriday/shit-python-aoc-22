import re

input = open("11/input.txt","r").read().split("\n\n")

def parse_monkey(text):
    id = int(re.search("Monkey (\d+)",text).groups()[0])
    left, op, right = re.search("Operation: new = (.+) (.) (.+)",text).groups()
    monkey = {
        "items": [int(i) for i in re.search("Starting items: (.*)",text).groups()[0].split(", ")],
        "op_left": left,
        "op": op,
        "op_right": right,
        "divisible_test": int(re.search("Test: divisible by (\d+)",text).groups()[0]),
        "true_monkey": int(re.search("If true: throw to monkey (\d+)",text).groups()[0]),
        "false_monkey": int(re.search("If false: throw to monkey (\d+)",text).groups()[0]),
        "inspected": 0
    }
    return [id, monkey]

def monkey_operation(value,left,op,right):
    left = value if left == "old" else int(left)
    right = value if right == "old" else int(right)
    if op == "+": result = left + right
    if op == "*": result = left * right
    return result

monkeys = {k:v for k,v in [parse_monkey(i) for i in input]}

for _ in range(20):
    for id, monkey in monkeys.items():
        while monkey["items"]:
            item = monkey["items"].pop(0)
            monkey["inspected"] += 1
            item = monkey_operation(item,monkey["op_left"],monkey["op"],monkey["op_right"])
            item = item // 3
            if item % monkey["divisible_test"] == 0:
                monkeys[monkey["true_monkey"]]["items"].append(item)
            else:
                monkeys[monkey["false_monkey"]]["items"].append(item)

sorted_counts = sorted([m["inspected"] for m in monkeys.values()])[-2:]
print(sorted_counts[0] * sorted_counts[1])

# part 2

monkeys = {k:v for k,v in [parse_monkey(i) for i in input]}

prime_factor_mod = 1
for v in monkeys.values():
    prime_factor_mod *= v["divisible_test"]

for _ in range(10000):
    for id, monkey in monkeys.items():
        while monkey["items"]:
            item = monkey["items"].pop(0)
            monkey["inspected"] += 1
            item = monkey_operation(item,monkey["op_left"],monkey["op"],monkey["op_right"])
            item = item % prime_factor_mod
            if item % monkey["divisible_test"] == 0:
                monkeys[monkey["true_monkey"]]["items"] += [item]
            else:
                monkeys[monkey["false_monkey"]]["items"] += [item]

sorted_counts = sorted([m["inspected"] for m in monkeys.values()])[-2:]
print(sorted_counts[0] * sorted_counts[1])