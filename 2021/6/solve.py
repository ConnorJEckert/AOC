

def star1():
    with open("input.txt") as fp:
        school = [int(x) for x in fp.readline().strip().split(",")]
        ages = [0,0,0,0,0,0,0,0,0]

        for age in school:
            ages[age] += 1

        for x in range(80):
            new_ages = [ages[1],ages[2],ages[3],ages[4],ages[5],ages[6],ages[7]+ages[0],ages[8],ages[0]]
            ages = new_ages

        print(sum(ages))


def star2():
    with open("input.txt") as fp:
        school = [int(x) for x in fp.readline().strip().split(",")]
        ages = [0,0,0,0,0,0,0,0,0]

        for age in school:
            ages[age] += 1

        for x in range(256):
            new_ages = [ages[1],ages[2],ages[3],ages[4],ages[5],ages[6],ages[7]+ages[0],ages[8],ages[0]]
            ages = new_ages

        print(sum(ages))

star2()