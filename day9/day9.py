##########
# PART 1 #
##########

"""
data = open("day9in.txt").read().split("\n")
last = []
for x in data:
    if (len(last) != 25): last.append(int(x))
    else:
        x = int(x)
        found = False
        for i in range(len(last)):
            for j in range(i + 1, len(last)):
                if ((last[i] + last[j]) == x):
                    found = True
                    break
            if (found): break
        if (not found):
            print(x)
            break

        last.pop(0)
        last.append(x)
"""

##########
# PART 2 #
##########

data = open("day9in.txt").read().split("\n")
last = []
target = None
nums = []
for x in data:
    x = int(x)
    nums.append(x)
    if (len(last) != 25): last.append(x)
    else:
        found = False
        for i in range(len(last)):
            for j in range(i + 1, len(last)):
                if ((last[i] + last[j]) == x):
                    found = True
                    break
            if (found): break
        if (not found):
            target = x
            break

        last.pop(0)
        last.append(x)
end = False
for i in range(len(nums)):
    j = i
    while (j < len(nums)):
        x = sum(nums[i : j + 1])
        if (x > target): break
        if (x == target):
            x = nums[i : j + 1]
            print(min(x) + max(x))
            end = True
            break
        j += 1
    if (end): break