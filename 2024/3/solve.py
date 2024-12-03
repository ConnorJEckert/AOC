import re

def star1():
    with open("input.txt") as fp:
        lines = fp.read()
        result = calculate_mul_sum(lines)
        print(result)
        return result

def calculate_mul_sum(corrupted_memory: str) -> int:
    """
    Scans a given corrupted memory string for valid mul(X,Y) instructions
    and returns the sum of their results.
    
    :param corrupted_memory: A string containing corrupted memory data.
    :return: The sum of results from all valid mul(X,Y) instructions.
    """
    # Regex pattern to match valid mul(X,Y) instructions
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)
    
    # Calculate and return the sum of all valid multiplication results
    return sum(int(x) * int(y) for x, y in matches)

def calculate_conditional_mul_sum(corrupted_memory: str) -> int:
    """
    Scans the given corrupted memory for valid mul(X,Y) instructions,
    respecting the enabling and disabling behavior of do() and don't() instructions.
    
    :param corrupted_memory: A string containing corrupted memory data.
    :return: The sum of results from all enabled mul(X,Y) instructions.
    """
    # Regex patterns for instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Initialize variables
    enabled = True  # Multiplication instructions are enabled by default
    result_sum = 0

    # Split the memory into tokens to process sequentially
    tokens = re.split(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", corrupted_memory)

    for token in tokens:
        token = token.strip()  # Clean up whitespace

        if re.match(do_pattern, token):
            enabled = True
        elif re.match(dont_pattern, token):
            enabled = False
        elif re.match(mul_pattern, token) and enabled:
            # Extract numbers and perform multiplication
            x, y = map(int, re.findall(r"\d+", token))
            result_sum += x * y

    return result_sum

def star2():
    with open("input.txt") as fp:
        lines = fp.read()
        
        result = calculate_conditional_mul_sum(lines)
        print(result)
        return result


star2()


