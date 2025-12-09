import re

def sum_invalid_ids_regex(range_str):
    """
    Sum all invalid IDs using regex.
    Pattern ^(.+)\1+$ matches a pattern repeated at least twice.
    """
    start, end = map(int, range_str.split('-'))
    return sum(num for num in range(start, end + 1) if re.match(r'^(.+)\1+$', str(num)))

result = 0 
with open("input.txt") as fp:
    lines = fp.readline()
    lines = lines.split(",")
    for line in lines:
        result += sum_invalid_ids_regex(line)
print(result)