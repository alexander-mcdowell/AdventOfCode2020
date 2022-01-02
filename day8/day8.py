##########
# PART 1 #
##########

"""
data = open("day8in.txt").read().split("\n")
instructions = []
for inst in data:
    op, val = inst.split(" ")
    instructions.append((op, int(val)))
i = 0
ran = []
acc = 0
while (i < len(instructions)):
    if (i in ran): break
    ran.append(i)
    op, val = instructions[i]
    if (op == "jmp"): i += val
    else:
        if (op == "acc"): acc += val
        i += 1
print(acc)
"""

##########
# PART 2 #
##########

data = open("day8in.txt").read().split("\n")
instructions = []
for inst in data:
    op, val = inst.split(" ")
    instructions.append((op, int(val)))

def terminates(instructions):
    i = 0
    ran = []
    acc = 0
    while (i < len(instructions)):
        if (i in ran): return False, acc
        ran.append(i)
        op, val = instructions[i]
        if (op == "jmp"): i += val
        else:
            if (op == "acc"): acc += val
            i += 1
    return True, acc

for i in range(len(instructions)):
    op, val = instructions[i]
    if (op == "nop"):
        term, acc = terminates(instructions[:i] + [("jmp", val)] + instructions[i + 1:])
        if (term):
            print(acc)
            break
    else:
        term, acc = terminates(instructions[:i] + [("nop", val)] + instructions[i + 1:])
        if (term):
            print(acc)
            break