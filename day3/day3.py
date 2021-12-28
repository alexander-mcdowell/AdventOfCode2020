##########
# PART 1 #
##########

"""
data = open("day3in.txt").read().split("\n")
grid = [list(x) for x in data]
n, m = len(grid), len(grid[0])

count = 0
x, y = 0, 0
while (True):
    x = (x + 3) % m
    y += 1
    
    if (y == n): break
    if (grid[y][x] == '#'): count += 1
print(count)
"""

##########
# PART 2 #
##########

data = open("day3in.txt").read().split("\n")
grid = [list(x) for x in data]
n, m = len(grid), len(grid[0])
move_types = [(1,1), (3,1), (5,1), (7,1), (1,2)]

prod = 1
for move in move_types:
    count = 0
    x, y = 0, 0
    while (True):
        x = (x + move[0]) % m
        y += move[1]
        
        if (y >= n): break
        if (grid[y][x] == '#'): count += 1
    prod *= count
print(prod)