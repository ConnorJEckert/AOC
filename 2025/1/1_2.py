cur_num = 50
count = 0

with open("input.txt") as fp:
    for line in fp.readlines():
        d = line[0]
        num = int(line[1:])
        
        if d == "L":
            # Going left, we hit 0 after: cur_num clicks, cur_num+100 clicks, etc.
            # But we need cur_num > 0 for the first hit
            if cur_num > 0 and num >= cur_num:
                count += ((num - cur_num) // 100) + 1
            elif cur_num == 0 and num >= 100:
                count += (num // 100)
            cur_num = (cur_num - num) % 100
            
        else:  # R
            # Going right, we hit 0 after: (100-cur_num) clicks
            distance_to_zero = 100 - cur_num
            if cur_num > 0 and num >= distance_to_zero:
                count += ((num - distance_to_zero) // 100) + 1
            elif cur_num == 0 and num >= 100:
                count += (num // 100)
            cur_num = (cur_num + num) % 100

print(count)