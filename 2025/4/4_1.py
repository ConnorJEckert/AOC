
adj = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def count_adj(grid, coord):
    count = 0
    y, x = coord
    if grid[y][x] == "@":
        for shift in adj:
            y2, x2 = shift
            new_x = x+x2
            new_y = y+y2
            if new_y >= 0 and new_x >= 0 and new_y < len(grid) and new_x < len(grid[0]) and grid[new_y][new_x] == "@":
                count += 1
    return count


with open("input.txt") as fp:
    grid = []
    y = 0
    count = 0
    for line in fp.readlines():
        line = line.strip()
        x_grid = [x for x in line]
        grid.append(x_grid)
    y_len = len(grid)
    x_len = len(grid[0])
    for y in range(y_len):
        for x in range(x_len):
            adj_count = count_adj(grid, (y,x))
            if adj_count < 4 and grid[y][x] == "@":
                count +=1
    print(count)

