##########
# PART 1 #
##########

"""
data = open("day1in.txt").read().split("\n")
nums = sorted([int(x) for x in data])

end = False
for i in range(len(nums)):
    x = nums[i]
    y = 2020 - x
    low, high = i, len(nums) - 1
    while (low <= high):
        mid = low + (high - low) // 2
        if (nums[mid] == y):
            end = True
            print(x, nums[mid], x * nums[mid])
            break
        if (nums[mid] > y): high = mid - 1
        else: low = mid + 1
            
    if (end): break
"""

##########
# PART 2 #
##########

data = open("day1in.txt").read().split("\n")
nums = sorted([int(x) for x in data])

end = False
for i in range(len(nums)):
    x = nums[i]
    for j in range(i + 1, len(nums)):
        y = nums[j]
        z = 2020 - x - y
        low, high = j, len(nums) - 1
        while (low <= high):
            mid = low + (high - low) // 2
            if (nums[mid] == z):
                end = True
                print(x, y, nums[mid], x * y * nums[mid])
                break
            if (nums[mid] > z): high = mid - 1
            else: low = mid + 1
                
        if (end): break
    if (end): break