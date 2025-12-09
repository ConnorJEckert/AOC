
cur_num = 50
count = 0

with open("input.txt") as fp:
    for line in fp.readlines():
        d = line[0]
        num = int(line[1:])
        if d == "L":
            cur_num = (cur_num - num) % 100
        else:
            cur_num = (cur_num + num) % 100
        if cur_num == 0:
            count += 1
print(count)

