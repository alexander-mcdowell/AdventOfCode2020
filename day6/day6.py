##########
# PART 1 #
##########

"""
data = open("day6in.txt").read().split("\n")
answered = 0
s = ""
for line in data:
    if (line == ""):
        answered += len(set(s))
        s = ""
    else: s += line
print(answered)
"""

##########
# PART 2 #
##########

def intersection(s, t):
    # Assume s and t are sorted
    u = ""
    for i in range(len(t)):
        if (t[i] in s): u += t[i]
    return u

data = open("day6in.txt").read().split("\n")
answered = 0
s = None
for line in data:
    if (line == ""):
        answered += len(s)
        s = None
    else:
        if (s == None): s = sorted(line)
        else: s = intersection(s, sorted(line))
print(answered)