
def injest_input(lines):
    cols = len(lines[0].strip().split())
    problems = [[] for _ in range(cols)]
    
    for col in range(cols):
        for line in lines:
            item = line.strip().split()[col]
            problems[col].append(item)
    return problems

def convert_problem(problem):
    max_c = get_max_colum(problem)
    # new_problem = []
    # for idx in range(max_c):
    #     for item in problem[:-1]:
    #         digit = item[0]
    #         new_problem[]
    return problem

def solve_problem(problem):
    problem = convert_problem(problem)
    op = problem[-1]
    if op == "*":
        result = 1
        for item in problem[:-1]:
            result *= int(item)
    else:
        result = 0
        for item in problem[:-1]:
            result += int(item)
    return result

def get_max_colum(problem):
    max_c = 0
    for item in problem[:-1]:
        max_c = max(max_c, len(item))
    return max_c

with open("input.txt") as fp:
    lines = fp.readlines()
    problems = injest_input(lines)
    output = 0
    for problem in problems:
        output += solve_problem(problem)
    print(output)
