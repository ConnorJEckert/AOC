import re

def find_largest(bank):
    for num in range(99,0,-1):
        if contains(str(num), bank):
            return num
    return None

def contains(target, source):
    return re.search('.*'.join(target), source) is not None

sum = 0
with open("input.txt") as fp:
    for line in fp.readlines():
        bank = line.strip()
        result = find_largest(bank)
        sum += result
print(sum)