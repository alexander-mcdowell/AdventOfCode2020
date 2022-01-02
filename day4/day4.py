##########
# PART 1 #
##########

"""
data = open("day4in.txt").read().split("\n")
passports = []
passport = {}
for line in data:
    if (line == ""):
        passports.append(passport)
        passport = {}
    else:
        for x in line.split(" "):
            k, v = x.split(":")
            passport[k] = v

valid = 0
for passport in passports:
    fields = [k for k in passport]
    if (len(fields) == 8 or (len(fields) == 7 and "cid" not in fields)): valid += 1
print(valid)
"""

##########
# PART 2 #
##########

data = open("day4in.txt").read().split("\n")
passports = []
passport = {}
for line in data:
    if (line == ""):
        passports.append(passport)
        passport = {}
    else:
        for x in line.split(" "):
            k, v = x.split(":")
            if (k != "cid"): passport[k] = v

valid = 0
for passport in passports:
    if (len(passport) != 7): continue
    satisfied = 0
    for k in passport:
        if (k not in ["byr", "iyr", "eyr", "ecl", "pid", "hcl", "hgt"]): break

        try:
            if (k == "byr" and not (1920 <= int(passport[k]) <= 2002)): break
            elif (k == "iyr" and not (2010 <= int(passport[k]) <= 2020)): break
            elif (k == "eyr" and not (2020 <= int(passport[k]) <= 2030)): break
            elif (k == "ecl" and passport[k] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]): break
            elif (k == "pid" and (len(str(passport[k])) != 9)): break
            elif (k == "hcl"):
                if (type(passport[k]) != str or passport[k][0] != '#' or len(passport[k]) != 7): break
                x = passport[k][1:]
                if (len(x) != 6): break
                for c in x:
                    if (c not in "0123456789abcdef"): break
            elif (k == "hgt"):
                if (type(passport[k]) != str): break
                height = ""
                i = 0
                while (i < len(passport[k])):
                    c = passport[k][i]
                    if (c in "0123456789"): height += c
                    else: break
                    i += 1
                if (i == len(passport[k])): break
                height = int(height)
                if (passport[k][i:] == "cm" and not (150 <= height <= 193)): break
                elif (passport[k][i:] == "in" and not (59 <= height <= 76)): break
        except Exception as _: pass
        satisfied += 1

    if (satisfied == 7): valid += 1

print(valid)