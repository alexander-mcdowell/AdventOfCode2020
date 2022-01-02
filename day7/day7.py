##########
# PART 1 #
##########

"""
data = open("day7in.txt").read().split("\n")
bags = {}
for line in data:
    container, contained = line.split(" bags contain ")
    if (contained == "no other bags."): bags[container] = None
    else:
        bags[container] = []
        if (", " not in contained):
            contained = contained[:-1]
            if (contained[-1] == 's'): contained = contained[:-1]
            y = contained.split(" ")
            num, bag = int(y[0]), " ".join(y[1:-1])
            bags[container].append((num, bag))
        else:   
            contained = contained.split(", ")
            for i in range(len(contained)):
                x = contained[i]
                if (i == len(contained) - 1): x = x[:-1]
                y = x.split(" ")
                num, bag = int(y[0]), " ".join(y[1:-1])
                bags[container].append((num, bag))

def can_hold(bag, bag_type, bags):
    if (bag == bag_type): return True
    if (bags[bag] == None): return False
    for k in bags[bag]:
        if (can_hold(k[1], bag_type, bags)): return True
    return False

x = 0
for k in bags:
    if (can_hold(k, "shiny gold", bags)): x += 1
print(x - 1)
"""

##########
# PART 2 #
##########

data = open("day7in.txt").read().split("\n")
bags = {}
for line in data:
    container, contained = line.split(" bags contain ")
    if (contained == "no other bags."): bags[container] = None
    else:
        bags[container] = []
        if (", " not in contained):
            contained = contained[:-1]
            if (contained[-1] == 's'): contained = contained[:-1]
            y = contained.split(" ")
            num, bag = int(y[0]), " ".join(y[1:-1])
            bags[container].append((num, bag))
        else:   
            contained = contained.split(", ")
            for i in range(len(contained)):
                x = contained[i]
                if (i == len(contained) - 1): x = x[:-1]
                y = x.split(" ")
                num, bag = int(y[0]), " ".join(y[1:-1])
                bags[container].append((num, bag))

def recurse(bag, bags):
    if (bags[bag] == None): return 1
    num = 1
    for k in bags[bag]: num += k[0] * recurse(k[1], bags)
    return num

print(recurse("shiny gold", bags) - 1)