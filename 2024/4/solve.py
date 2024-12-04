def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    directions = [
        (0, 1),  # Horizontal right
        (1, 0),  # Vertical down
        (1, 1),  # Diagonal down-right
        (1, -1), # Diagonal down-left
        (0, -1), # Horizontal left
        (-1, 0), # Vertical up
        (-1, -1),# Diagonal up-left
        (-1, 1)  # Diagonal up-right
    ]

    def is_valid(x, y, dx, dy, word_length):
        # Check if the word can fit starting at (x, y) in direction (dx, dy)
        for k in range(word_length):
            nx, ny = x + k * dx, y + k * dy
            if not (0 <= nx < rows and 0 <= ny < cols):
                return False
        return True

    def check_direction(x, y, dx, dy):
        if not is_valid(x, y, dx, dy, len(word)):
            return False
        for k in range(len(word)):
            nx, ny = x + k * dx, y + k * dy
            if grid[nx][ny] != word[k]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1
    return count

def star1():
    with open("input.txt") as fp:
        grid = [line.strip() for line in fp.readlines()]
        result = count_xmas(grid)
    return result

def searchWord(grid, r, c, m, n):

    if grid[r][c] != "A":
        return 0

    dirs = ((-1, -1, 1, 1),(-1, 1, 1, -1)) 

    x_mas_leg_count = 0
    for r1, c1, r2, c2 in dirs:
        if not (0 <= r+r1 < m) or not (0 <= r+r2 < m):
            continue
        
        if not (0 <= c+c1 < n) or not (0 <= c+c2 < n):
            continue

        if grid[r+r1][c+c1] == "S" and grid[r+r2][c+c2] == "M": 
            x_mas_leg_count += 1      
        elif grid[r+r1][c+c1] == "M" and grid[r+r2][c+c2] == "S":
            x_mas_leg_count += 1

    if x_mas_leg_count == 2:
        return 1
    return 0


def star2():
    with open("input.txt") as fp:
        grid = [line.strip() for line in fp.readlines()]
        n = len(grid[0])
        m = len(grid)
        result = 0
        for i in range(0, m):
            for j in range(0, n):
                result += searchWord(grid, i, j, m, n)
    return result

# Call the function with the grid
result = star2()
print("Total occurrences of XMAS:", result)
