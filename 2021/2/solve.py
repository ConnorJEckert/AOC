
def star1():
    with open("input.txt") as fp:
        x = 0
        y = 0

        for line in fp:
            order = line.strip().split(" ")
            direction = order[0]
            magnitude = int(order[1])

            if direction == "forward":
                x += magnitude
            elif direction == "down":
                y += magnitude
            elif direction == "up":
                y -= magnitude
            else:
                print("bad instruction")
                return()
        
        print(x*y)

def star2():
    with open("input.txt") as fp:
        x = 0
        y = 0
        a = 0

        for line in fp:
            order = line.strip().split(" ")
            direction = order[0]
            magnitude = int(order[1])

            if direction == "forward":
                x += magnitude
                y += a*magnitude
            elif direction == "down":
                a += magnitude
            elif direction == "up":
                a -= magnitude
            else:
                print("bad instruction")
                return()
        
        print(x*y)


star2()