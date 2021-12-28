##########
# PART 1 #
##########

"""
import math

def flipX(grid):
    grid_copy = [[grid[i][j] for j in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid) // 2):
            grid_copy[i][j] = grid[i][len(grid) - 1 - j]
            grid_copy[i][len(grid) - 1 - j] = grid[i][j]
    return grid_copy
            
def flipY(grid):
    grid_copy = [[grid[i][j] for j in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid) // 2):
        for j in range(len(grid)):
            grid_copy[i][j] = grid[len(grid) - 1 - i][j]
            grid_copy[len(grid) - 1 - i][j] = grid[i][j]
    return grid_copy

def rotate(grid):
    grid_copy = [[grid[i][j] for j in range(len(grid))] for i in range(len(grid))]
    n = len(grid) // 2
    k = 1 if (len(grid) % 2 == 0) else 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_copy[n - (j - n) - k][(i - n) + n] = grid[i][j]
    return grid_copy
    
def check_align(grid1, grid2, dir):
    # Up
    if (dir == 0):
        return grid1[0] == grid2[-1]
    # Left
    elif (dir == 1):
        col1 = [grid1[i][0] for i in range(len(grid1))]
        col2 = [grid2[i][-1] for i in range(len(grid1))]
        return col1 == col2
    # Down
    elif (dir == 2):
        return grid1[-1] == grid2[0]
    # Right
    else:
        col1 = [grid1[i][-1] for i in range(len(grid1))]
        col2 = [grid2[i][0] for i in range(len(grid1))]
        return col1 == col2

data = open("day20in.txt").read().split("\n")
grids = {}
keys = []
key, grid = None, None
for line in data:
    if (line == ""): grids[key] = grid
    elif ("Tile" in line):
        grid = []
        key = int(line.split("Tile ")[1][:-1])
        keys.append(key)
    else: grid.append(list(line))

key_to_pos = {keys[0]: (0, 0)}
pos_to_key = {(0, 0): keys[0]}
queue = [keys[0]]
while (len(queue) != 0):
    key = queue.pop(0)
    pos = key_to_pos[key]
    for u in keys:
        if (key == u or u in key_to_pos): continue
        
        for _ in range(4):
            for _ in range(2):
                for _ in range(2):
                    valid = True
                    # Check top of key's grid and bottom of u's grid
                    if (check_align(grids[key], grids[u], 0)):
                        # Check up from u
                        if ((pos[0] - 2, pos[1]) in pos_to_key):
                            v = pos_to_key[(pos[0] - 2, pos[1])]
                            if (not check_align(grids[u], grids[v], 0)): valid = False
                        # Check left from u
                        if ((pos[0] - 1, pos[1] - 1) in pos_to_key):
                            v = pos_to_key[(pos[0] - 1, pos[1] - 1)]
                            if (not check_align(grids[u], grids[v], 1)): valid = False
                        # Check right from u
                        if ((pos[0] - 1, pos[1] + 1) in pos_to_key):
                            v = pos_to_key[(pos[0] - 1, pos[1] + 1)]
                            if (not check_align(grids[u], grids[v], 3)): valid = False
                        
                        if (valid):
                            #print("Up", key, u)
                            key_to_pos[u] = (pos[0] - 1, pos[1])
                            pos_to_key[(pos[0] - 1, pos[1])] = u
                            queue.append(u)
                            break

                    # Check bottom of key's grid and top of u's grid
                    elif (check_align(grids[key], grids[u], 2)):
                        # Check bottom from u
                        if ((pos[0] + 2, pos[1]) in pos_to_key):
                            v = pos_to_key[(pos[0] + 2, pos[1])]
                            if (not check_align(grids[u], grids[v], 2)): valid = False
                        # Check left from u
                        if ((pos[0] + 1, pos[1] - 1) in pos_to_key):
                            v = pos_to_key[(pos[0] + 1, pos[1] - 1)]
                            if (not check_align(grids[u], grids[v], 1)): valid = False
                        # Check right from u
                        if ((pos[0] + 1, pos[1] + 1) in pos_to_key):
                            v = pos_to_key[(pos[0] + 1, pos[1] + 1)]
                            if (not check_align(grids[u], grids[v], 3)): valid = False
                        
                        if (valid):
                            #print("Bottom", key, u)
                            key_to_pos[u] = (pos[0] + 1, pos[1])
                            pos_to_key[(pos[0] + 1, pos[1])] = u
                            queue.append(u)
                            break

                    # Check left of key's grid and right of u's grid
                    elif (check_align(grids[key], grids[u], 1)):
                        # Check up from u
                        if ((pos[0] - 1, pos[1] - 1) in pos_to_key):
                            v = pos_to_key[(pos[0] - 1, pos[1] - 1)]
                            if (not check_align(grids[u], grids[v], 0)): valid = False
                        # Check left from u
                        if ((pos[0], pos[1] - 2) in pos_to_key):
                            v = pos_to_key[(pos[0], pos[1] - 2)]
                            if (not check_align(grids[u], grids[v], 1)): valid = False
                        # Check down from u
                        if ((pos[0] + 1, pos[1] - 1) in pos_to_key):
                            v = pos_to_key[(pos[0] + 1, pos[1] - 1)]
                            if (not check_align(grids[u], grids[v], 2)): valid = False
                        
                        if (valid):
                            #print("Left", key, u)
                            key_to_pos[u] = (pos[0], pos[1] - 1)
                            pos_to_key[(pos[0], pos[1] - 1)] = u
                            queue.append(u)
                            break

                    # Check right of key's grid and left of u's grid
                    elif (check_align(grids[key], grids[u], 3)):
                        # Check up from u
                        if ((pos[0] - 1, pos[1] + 1) in pos_to_key):
                            v = pos_to_key[(pos[0] - 1, pos[1] + 1)]
                            if (not check_align(grids[u], grids[v], 0)): valid = False
                        # Check down from u
                        if ((pos[0] + 1, pos[1] + 1) in pos_to_key):
                            v = pos_to_key[(pos[0] + 1, pos[1] + 1)]
                            if (not check_align(grids[u], grids[v], 2)): valid = False
                        # Check right from u
                        if ((pos[0], pos[1] + 2) in pos_to_key):
                            v = pos_to_key[(pos[0], pos[1] + 2)]
                            if (not check_align(grids[u], grids[v], 3)): valid = False
                        
                        if (valid):
                            #print("Right", key, u)
                            key_to_pos[u] = (pos[0], pos[1] + 1)
                            pos_to_key[(pos[0], pos[1] + 1)] = u
                            queue.append(u)
                            break
                    else: valid = False
                    
                    if (valid): break
                    grids[u] = flipX(grids[u])
                if (valid): break
                grids[u] = flipY(grids[u])
            if (valid): break
            grids[u] = rotate(grids[u])

# Find the top left corner as a reference
top_left_key = None
for key in key_to_pos:
    pos = key_to_pos[key]
    # There must only be two outgoing nodes: left and right
    if ((pos[0] + 1, pos[1]) in pos_to_key and (pos[0], pos[1] + 1) in pos_to_key
        and (pos[0] - 1, pos[1]) not in pos_to_key and (pos[0], pos[1] - 1) not in pos_to_key):
        top_left_key = key
        break

n = int(math.sqrt(len(keys)))
image = [[None for _ in range(n)] for _ in range(n)]

# Move from top-left to bottom-right
queue = [(top_left_key, 0, 0)]
visited = {k: False for k in keys}
while (len(queue) != 0):
    key, i, j = queue.pop(0)
    if (visited[key]): continue
    visited[key] = True
    image[i][j] = key
    pos = key_to_pos[key]
    
    # Check right
    if ((pos[0], pos[1] + 1) in pos_to_key):
        next_key = pos_to_key[(pos[0], pos[1] + 1)]
        queue.append((next_key, i, j + 1))
    # Check down
    if ((pos[0] + 1, pos[1]) in pos_to_key):
        next_key = pos_to_key[(pos[0] + 1, pos[1])]
        queue.append((next_key, i + 1, j))

print(image[0][0] * image[-1][0] * image[0][-1] * image[-1][-1])
"""

##########
# PART 2 #
##########

import math

def flipX(grid):
    grid_copy = [[grid[i][j] for j in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid) // 2):
            grid_copy[i][j] = grid[i][len(grid) - 1 - j]
            grid_copy[i][len(grid) - 1 - j] = grid[i][j]
    return grid_copy
            
def flipY(grid):
    grid_copy = [[grid[i][j] for j in range(len(grid))] for i in range(len(grid))]
    for i in range(len(grid) // 2):
        for j in range(len(grid)):
            grid_copy[i][j] = grid[len(grid) - 1 - i][j]
            grid_copy[len(grid) - 1 - i][j] = grid[i][j]
    return grid_copy

def rotate(grid):
    grid_copy = [[grid[i][j] for j in range(len(grid))] for i in range(len(grid))]
    n = len(grid) // 2
    k = 1 if (len(grid) % 2 == 0) else 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid_copy[n - (j - n) - k][(i - n) + n] = grid[i][j]
    return grid_copy
    
def check_align(grid1, grid2, dir):
    # Up
    if (dir == 0):
        return grid1[0] == grid2[-1]
    # Left
    elif (dir == 1):
        col1 = [grid1[i][0] for i in range(len(grid1))]
        col2 = [grid2[i][-1] for i in range(len(grid1))]
        return col1 == col2
    # Down
    elif (dir == 2):
        return grid1[-1] == grid2[0]
    # Right
    else:
        col1 = [grid1[i][-1] for i in range(len(grid1))]
        col2 = [grid2[i][0] for i in range(len(grid1))]
        return col1 == col2

data = open("day20in.txt").read().split("\n")
grids = {}
keys = []
key, grid = None, None
for line in data:
    if (line == ""): grids[key] = grid
    elif ("Tile" in line):
        grid = []
        key = int(line.split("Tile ")[1][:-1])
        keys.append(key)
    else: grid.append(list(line))

key_to_pos = {keys[0]: (0, 0)}
pos_to_key = {(0, 0): keys[0]}
queue = [keys[0]]
while (len(queue) != 0):
    key = queue.pop(0)
    pos = key_to_pos[key]
    for u in keys:
        if (key == u or u in key_to_pos): continue
        
        for _ in range(4):
            for _ in range(2):
                for _ in range(2):
                    valid = True
                    # Check top of key's grid and bottom of u's grid
                    if (check_align(grids[key], grids[u], 0)):
                        # Check up from u
                        if ((pos[0] - 2, pos[1]) in pos_to_key):
                            v = pos_to_key[(pos[0] - 2, pos[1])]
                            if (not check_align(grids[u], grids[v], 0)): valid = False
                        # Check left from u
                        if ((pos[0] - 1, pos[1] - 1) in pos_to_key):
                            v = pos_to_key[(pos[0] - 1, pos[1] - 1)]
                            if (not check_align(grids[u], grids[v], 1)): valid = False
                        # Check right from u
                        if ((pos[0] - 1, pos[1] + 1) in pos_to_key):
                            v = pos_to_key[(pos[0] - 1, pos[1] + 1)]
                            if (not check_align(grids[u], grids[v], 3)): valid = False
                        
                        if (valid):
                            #print("Up", key, u)
                            key_to_pos[u] = (pos[0] - 1, pos[1])
                            pos_to_key[(pos[0] - 1, pos[1])] = u
                            queue.append(u)
                            break

                    # Check bottom of key's grid and top of u's grid
                    elif (check_align(grids[key], grids[u], 2)):
                        # Check bottom from u
                        if ((pos[0] + 2, pos[1]) in pos_to_key):
                            v = pos_to_key[(pos[0] + 2, pos[1])]
                            if (not check_align(grids[u], grids[v], 2)): valid = False
                        # Check left from u
                        if ((pos[0] + 1, pos[1] - 1) in pos_to_key):
                            v = pos_to_key[(pos[0] + 1, pos[1] - 1)]
                            if (not check_align(grids[u], grids[v], 1)): valid = False
                        # Check right from u
                        if ((pos[0] + 1, pos[1] + 1) in pos_to_key):
                            v = pos_to_key[(pos[0] + 1, pos[1] + 1)]
                            if (not check_align(grids[u], grids[v], 3)): valid = False
                        
                        if (valid):
                            #print("Bottom", key, u)
                            key_to_pos[u] = (pos[0] + 1, pos[1])
                            pos_to_key[(pos[0] + 1, pos[1])] = u
                            queue.append(u)
                            break

                    # Check left of key's grid and right of u's grid
                    elif (check_align(grids[key], grids[u], 1)):
                        # Check up from u
                        if ((pos[0] - 1, pos[1] - 1) in pos_to_key):
                            v = pos_to_key[(pos[0] - 1, pos[1] - 1)]
                            if (not check_align(grids[u], grids[v], 0)): valid = False
                        # Check left from u
                        if ((pos[0], pos[1] - 2) in pos_to_key):
                            v = pos_to_key[(pos[0], pos[1] - 2)]
                            if (not check_align(grids[u], grids[v], 1)): valid = False
                        # Check down from u
                        if ((pos[0] + 1, pos[1] - 1) in pos_to_key):
                            v = pos_to_key[(pos[0] + 1, pos[1] - 1)]
                            if (not check_align(grids[u], grids[v], 2)): valid = False
                        
                        if (valid):
                            #print("Left", key, u)
                            key_to_pos[u] = (pos[0], pos[1] - 1)
                            pos_to_key[(pos[0], pos[1] - 1)] = u
                            queue.append(u)
                            break

                    # Check right of key's grid and left of u's grid
                    elif (check_align(grids[key], grids[u], 3)):
                        # Check up from u
                        if ((pos[0] - 1, pos[1] + 1) in pos_to_key):
                            v = pos_to_key[(pos[0] - 1, pos[1] + 1)]
                            if (not check_align(grids[u], grids[v], 0)): valid = False
                        # Check down from u
                        if ((pos[0] + 1, pos[1] + 1) in pos_to_key):
                            v = pos_to_key[(pos[0] + 1, pos[1] + 1)]
                            if (not check_align(grids[u], grids[v], 2)): valid = False
                        # Check right from u
                        if ((pos[0], pos[1] + 2) in pos_to_key):
                            v = pos_to_key[(pos[0], pos[1] + 2)]
                            if (not check_align(grids[u], grids[v], 3)): valid = False
                        
                        if (valid):
                            #print("Right", key, u)
                            key_to_pos[u] = (pos[0], pos[1] + 1)
                            pos_to_key[(pos[0], pos[1] + 1)] = u
                            queue.append(u)
                            break
                    else: valid = False
                    
                    if (valid): break
                    grids[u] = flipX(grids[u])
                if (valid): break
                grids[u] = flipY(grids[u])
            if (valid): break
            grids[u] = rotate(grids[u])

# Find the top left corner as a reference
top_left_key = None
for key in key_to_pos:
    pos = key_to_pos[key]
    # There must only be two outgoing nodes: left and right
    if ((pos[0] + 1, pos[1]) in pos_to_key and (pos[0], pos[1] + 1) in pos_to_key
        and (pos[0] - 1, pos[1]) not in pos_to_key and (pos[0], pos[1] - 1) not in pos_to_key):
        top_left_key = key
        break

n = int(math.sqrt(len(keys)))
image_keys = [[None for _ in range(n)] for _ in range(n)]

# Move from top-left to bottom-right
queue = [(top_left_key, 0, 0)]
visited = {k: False for k in keys}
while (len(queue) != 0):
    key, i, j = queue.pop(0)
    if (visited[key]): continue
    visited[key] = True
    image_keys[i][j] = key
    pos = key_to_pos[key]
    
    # Check right
    if ((pos[0], pos[1] + 1) in pos_to_key):
        next_key = pos_to_key[(pos[0], pos[1] + 1)]
        queue.append((next_key, i, j + 1))
    # Check down
    if ((pos[0] + 1, pos[1]) in pos_to_key):
        next_key = pos_to_key[(pos[0] + 1, pos[1])]
        queue.append((next_key, i + 1, j))

image_str = ""
for i in range(n):
    for k in range(1, len(grid) - 1):
        for j in range(n):
            grid = grids[image_keys[i][j]]
            image_str += "".join(grid[k][1:-1])

image = []
N = (len(grids[keys[0]]) - 2) * n
i = 0
row = []
for c in image_str:
    row.append(c)
    i += 1
    if (i == N):
        i = 0
        image.append(row)
        row = []

pattern = [list(s) for s in "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   ".split("\n")]
pattern_n, pattern_m = len(pattern), len(pattern[0])

end = False
for _ in range(4):
    for _ in range(2):
        for _ in range(2):
            included = []
            count = 0
            
            for i in range(len(image) - pattern_n):
                for j in range(len(image) - pattern_m):
                    possibly_included = []
                    valid = True
                    for n in range(pattern_n):
                        for m in range(pattern_m):
                            if (image[i + n][j + m] != '#' and pattern[n][m] == "#"):
                                valid = False
                                break
                            elif (image[i + n][j + m] == "#" and pattern[n][m] == "#"):
                                possibly_included.append((i + n, j + m))
                                
                        if (not valid): break
                    if (valid):
                        count += 1
                        for x in possibly_included:
                            if x not in included: included.append(x)
            if (count != 0):
                end = True
                total = 0
                for x in image:
                    for y in x:
                        if (y == '#'): total += 1
                print(total - len(included))
                break
            
            image = flipX(image)

        if (end): break
        image = flipY(image)
    
    if (end): break
    image = rotate(image)