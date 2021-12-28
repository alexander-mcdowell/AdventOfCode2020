##########
# PART 2 #
##########

"""
data = open("day2in.txt").read().split("\n")
count = 0
for line in data:
    occurs, c, s = line.split(" ")
    low, high = [int(x) for x in occurs.split("-")]
    c = c[:-1]
    if (low <= s.count(c) <= high): count += 1
print(count)
"""

##########
# PART 2 #
##########

data = open("day2in.txt").read().split("\n")
count = 0
for line in data:
    nums, c, s = line.split(" ")
    low, high = [int(x) - 1 for x in nums.split("-")]
    c = c[:-1]
    if ((s[low] == c) ^ (s[high] == c)): count += 1
print(count)