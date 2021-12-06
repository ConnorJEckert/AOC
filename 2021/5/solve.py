def star1():
    with open('input.txt') as fp: 
        lines = [list(map(int, line.strip().replace('->', ',').split(',')))for line in fp]

    max_x = max(max([(coord[0], coord[2])for coord in lines])) + 1
    max_y = max(max([(coord[1], coord[3])for coord in lines])) + 1

    matrix = [[0 for i in range(max_x)] for j in range(max_y)]

    for x1, y1, x2, y2 in lines:
        min_x, dx = min(x1, x2), abs(x2 - x1)
        min_y, dy = min(y1, y2), abs(y2 - y1)
        if x1 == x2:
            for i in range(dy + 1):
                matrix[i + min_y][x1] += 1
        elif y1 == y2:
            for i in range(dx + 1):
                matrix[y1][i + min_x] += 1

    print(sum([1 for line in matrix for num in line if num > 1]))


def star2():
    with open('input.txt') as fp: 
        lines = [list(map(int, line.strip().replace('->', ',').split(',')))for line in fp]

    max_x = max(max([(coord[0], coord[2])for coord in lines])) + 1
    max_y = max(max([(coord[1], coord[3])for coord in lines])) + 1

    matrix = [[0 for i in range(max_x)] for j in range(max_y)]

    for x1, y1, x2, y2 in lines:
        min_x, dx = min(x1, x2), abs(x2 - x1)
        min_y, dy = min(y1, y2), abs(y2 - y1)
        if x1 == x2:
            for i in range(dy + 1):
                matrix[i + min_y][x1] += 1
        elif y1 == y2:
            for i in range(dx + 1):
                matrix[y1][i + min_x] += 1
        else:
            cx = 1 if x2 > x1 else -1
            cy = 1 if y2 > y1 else -1
            for i in range(dx + 1):
                matrix[cy*i + y1][cx*i + x1] += 1

    print(sum([1 for line in matrix for num in line if num > 1]))


star2()