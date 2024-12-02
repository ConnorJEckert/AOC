def star1():
    with open("input.txt") as fp:
        count = 0
        for line in fp.readlines():
            if checkline(line.split()):
                count += 1
    return count

def star2():
    with open("input.txt") as fp:
        count = 0
        for line in fp.readlines():
            
            nums = line.split()

            safe = checkline(nums)
            if not safe:
                problem_damp_lines = []
                for i in range(len(nums)):
                    new_line = nums.copy()
                    del new_line[i]
                    problem_damp_lines.append(new_line)
                
                for problem_damp_line in problem_damp_lines:
                    if checkline(problem_damp_line):
                        safe = True
                        break

            if safe:
                count += 1


    return count

def checkline(line):
    safe = True
    inc = False
    dec = False


    for i in range(len(line)-1):
        cur = int(line[i])
        next = int(line[i+1])

        diff = abs(cur-next)
        sign = next > cur

        if diff < 1 or diff > 3:
            safe = False
            break

        if sign:
            inc = True
        else:
            dec = True
        
        if inc and dec:
            safe = False

            break

    return safe 



output = star2()
print(output)