

def day8_1():
    with open("day8_input.txt", "r") as fp:
        lines = fp.read().split("\n")
        acc = 0
        ip = 0
        executed = set()
        while(True):
            inst = lines[ip].split()[0]
            val = int(lines[ip].split()[1])
            executed.add(ip)
            print(str(ip) + ": " + inst + " " + str(val))
            if (inst == "nop"):
                ip += 1
            elif (inst == "acc"):
                acc += val
                ip += 1
            elif (inst == "jmp"):
                ip += val
            if (ip in executed):
                print("instruction " + str(ip) + " already executed")
                print("acc: " + str(acc))
                break

def day8_2():
    with open("day8_input.txt", "r") as fp:
        lines = fp.read().split("\n")
        for i in range(0, len(lines)):
            print("testing instruction: " + str(i))
            res = flip_run(i, lines)
            if (res[0] == 1):
                print(res[1])
                break

def flip_run(flip_i, lines):
    acc = 0
    ip = 0
    executed = set()
    while(True):
        inst = lines[ip].split()[0]
        val = int(lines[ip].split()[1])
        executed.add(ip)

        if (flip_i == ip):
            if (inst == "nop"):
                inst = "jmp"
            elif (inst == "jmp"):
                inst = "nop"

        if (inst == "nop"):
            ip += 1
        elif (inst == "acc"):
            acc += val
            ip += 1
        elif (inst == "jmp"):
            ip += val

        if (ip in executed):
            return (-1,-99)
        if (ip >= len(lines)-1):
            return (1, acc)
                           

day8_2()