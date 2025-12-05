with open("input.txt") as fp:
    lines = fp.read()
    categories = lines.split("\n\n")
    ranges = categories[0].strip()
    ranges = [x for x in ranges.split("\n")]
    
    range_list = []
    for r in ranges:
        nums = r.split("-")
        low_n = int(nums[0])
        high_n = int(nums[1])
        range_list.append((low_n, high_n))
    
    range_list.sort()

    merged = []
    for start, end in range_list:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    count = 0
    for start, end in merged:
        count += end - start + 1
    
    print(count)