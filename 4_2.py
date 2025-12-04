import copy

adj = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def count_adj(grid, coord):
    count = 0
    y, x = coord
    if grid[y][x] == "@":
        for shift in adj:
            y2, x2 = shift
            new_x = x+x2
            new_y = y+y2
            if new_y >= 0 and new_x >= 0 and new_y < len(grid) and new_x < len(grid[0]):
                if grid[new_y][new_x] == "@" or grid[new_y][new_x] == "x":
                    count += 1
    return count

def count_remove(grid):
    count = 0 
    y_len = len(grid)
    x_len = len(grid[0])
    for y in range(y_len):
        for x in range(x_len):
            adj_count = count_adj(grid, (y,x))
            if adj_count < 4 and grid[y][x] == "@":
                count +=1
                grid[y][x] = "x"
    return count, grid

def grid_remove_x(grid):
    y_len = len(grid)
    x_len = len(grid[0])
    for y in range(y_len):
        for x in range(x_len):
            if grid[y][x] == "x":
                grid[y][x] = "."
    return grid

with open("input.txt") as fp:
    grid = []
    count = 0
    for line in fp.readlines():
        line = line.strip()
        x_grid = [x for x in line]
        grid.append(x_grid)
    
    changed = True
    while changed:

        old_grid = copy.deepcopy(grid)

        removed, grid = count_remove(grid)
        count += removed
        grid = grid_remove_x(grid)

        if grid == old_grid:
            changed = False

    print(count)

