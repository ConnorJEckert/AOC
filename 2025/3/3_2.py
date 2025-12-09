import re

def find_largest(bank):
    n = len(bank)
    keep = 12
    
    result = []
    start = 0
    
    for pos in range(keep):
        remaining_needed = keep - pos - 1
        search_end = n - remaining_needed
        
        best_digit = bank[start]
        best_idx = start
        
        for i in range(start + 1, search_end):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_idx = i
                if best_digit == '9':
                    break
        
        result.append(best_digit)
        start = best_idx + 1
    
    return int(''.join(result))

sum = 0
with open("input.txt") as fp:
    for line in fp.readlines():
        bank = line.strip()
        result = find_largest(bank)
        sum += result

print(sum)