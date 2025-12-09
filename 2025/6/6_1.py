
def injest_input(lines):
    cols = len(lines[0].strip().split())
    problems = [[] for _ in range(cols)]
    
    for col in range(cols):
        for line in lines:
            item = line.strip().split()[col]
            problems[col].append(item)
    return problems

def solve_problem(problem):
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


with open("input.txt") as fp:
    lines = fp.readlines()
    problems = injest_input(lines)
    output = 0
    for problem in problems:
        output += solve_problem(problem)
    print(output)
