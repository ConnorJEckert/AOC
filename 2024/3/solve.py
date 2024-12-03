import re

def star1():
    with open("input.txt") as fp:
        lines = fp.readlines()
        stripped_lines = [line.rstrip('\n') for line in lines]
        result = parse_engine_schematic(stripped_lines)
        print(f"The sum of all part numbers is: {result}")

        return result

def star2():
    with open("input.txt") as fp:
        lines = fp.readlines()
        stripped_lines = [line.rstrip('\n') for line in lines]
        result = parse_engine_schematic_for_gears(stripped_lines)
        print(f"The sum of all gear ratios is: {result}")

        return result

def parse_engine_schematic(rows):
    total_sum = 0
    rows_count = len(rows)
    cols_count = len(rows[0])

    # Function to check if a cell contains a symbol
    def is_symbol(x, y):
        if 0 <= x < rows_count and 0 <= y < cols_count:
            char = rows[x][y]
            return not char.isdigit() and char != '.'
        return False

    # Iterate through each row and find all numbers
    for i, row in enumerate(rows):
        # Use regex to find consecutive digits (treating them as a single number)
        for match in re.finditer(r'\d+', row):
            number_start = match.start()
            number_end = match.end()
            number = int(row[number_start:number_end])

            # Check all adjacent cells for symbols
            has_symbol = False
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    # Check all columns spanned by the number
                    for col in range(number_start, number_end):
                        x, y = i + dx, col + dy
                        if is_symbol(x, y):
                            has_symbol = True
                            break
                    if has_symbol:
                        break
                if has_symbol:
                    break

            # Add the number to the total sum if it has an adjacent symbol
            if has_symbol:
                total_sum += number

    return total_sum


def parse_engine_schematic_for_gears(rows):
    rows_count = len(rows)
    cols_count = len(rows[0])
    total_gear_ratio_sum = 0

    # Function to extract all part numbers and their positions
    def extract_numbers():
        numbers = []
        for i, row in enumerate(rows):
            for match in re.finditer(r'\d+', row):
                start_col = match.start()
                end_col = match.end() - 1
                number = int(match.group())
                numbers.append((number, i, start_col, end_col))
        return numbers

    # Function to check if a gear (*) is adjacent to a given number
    def is_gear_adjacent_to_number(gear_row, gear_col, number_row, number_start_col, number_end_col):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip the gear's own position
                adj_row = gear_row + dx
                adj_col = gear_col + dy
                if number_row == adj_row and number_start_col <= adj_col <= number_end_col:
                    return True
        return False

    # Extract all numbers and their positions
    numbers = extract_numbers()

    # Iterate through the schematic to find gears (*)
    for i in range(rows_count):
        for j in range(cols_count):
            if rows[i][j] == "*":  # Found a gear
                adjacent_numbers = []

                # Check each number to see if it's adjacent to this gear
                for number, number_row, number_start_col, number_end_col in numbers:
                    if is_gear_adjacent_to_number(i, j, number_row, number_start_col, number_end_col):
                        adjacent_numbers.append(number)

                # If exactly two numbers are adjacent, calculate the gear ratio
                if len(adjacent_numbers) == 2:
                    gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                    total_gear_ratio_sum += gear_ratio

    return total_gear_ratio_sum
star2()


