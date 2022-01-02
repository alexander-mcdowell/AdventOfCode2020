##########
# PART 1 #
##########

"""
data = open("day5in.txt").read().split("\n")
highest = 0
for id in data:
    low, mid, high = 0, None, 127
    i = 0
    while (i < len(id) - 3):
        mid = (low + high + 1) // 2
        if (id[i] == 'F'):
            high = mid - 1
            mid = high
        else:
            low = mid
            mid = low
        i += 1
    row = mid
    low, mid, high = 0, None, 7
    while (i < len(id)):
        mid = (low + high + 1) // 2
        if (id[i] == 'L'):
            high = mid - 1
            mid = high
        else:
            low = mid
            mid = low
        i += 1
    col = mid
    
    id = 8 * row + col
    if (id > highest): highest = id
print(highest)
"""

##########
# PART 2 #
##########

data = open("day5in.txt").read().split("\n")
ids = []
for id in data:
    low, mid, high = 0, None, 127
    i = 0
    while (i < len(id) - 3):
        mid = (low + high + 1) // 2
        if (id[i] == 'F'):
            high = mid - 1
            mid = high
        else:
            low = mid
            mid = low
        i += 1
    row = mid
    low, mid, high = 0, None, 7
    while (i < len(id)):
        mid = (low + high + 1) // 2
        if (id[i] == 'L'):
            high = mid - 1
            mid = high
        else:
            low = mid
            mid = low
        i += 1
    col = mid
    
    id = 8 * row + col
    ids.append(id)
ids = sorted(ids)

for i in range(len(ids) - 1):
    if (ids[i + 1] - ids[i] == 2):
        print(ids[i] + 1)
        break