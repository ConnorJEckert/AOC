
def decode(s, en): 

    dlen = {2:1, 4:4, 3:7, 7:8}
    dlett = {2:'', 4:'', 3:''}

    if dlen.get(len(s)):
        return dlen[len(s)] 

    for d in dlett.keys():
        dlett[d] = set([x for x in en if len(x) == d][0]) 

    ss = set(s)
    if len(ss) == 6:
        if not dlett[2].issubset(ss): 
            return 6
        else:
            if dlett[4].issubset(ss):
                return 9 
            else:
                return 0 

    if dlett[2].issubset(ss):
        return 3 
    else:
        if len(dlett[4]-ss) == 2:
            return 2 
        else:
            return 5 



def star1():
    with open("input.txt") as fp:
        inputs = [x.replace(' | ',' ').split() for x in fp.readlines()]
        outputs = sum([x[-4:] for x in inputs],[])
        outputs1478 = [x for x in outputs if len(x) != 5 and len(x) != 6]
        print(len(outputs1478))


def star2():
    with open("input.txt") as fp:
        inputs = [x.replace(' | ',' ').split() for x in fp.readlines()]
        sum = 0
        for num in inputs:
            for i in range(4):
                sum += decode(num[-i-1],num)*(10**i)
        print(sum)
        

star2()