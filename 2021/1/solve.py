


def star1():
    with open("input.txt", 'r') as fp:

        count = 0
        prev_depth = float('inf')

        for line in fp:
            cur_depth = int(line.strip())
            if (cur_depth > prev_depth): count +=1
            prev_depth = cur_depth

        print(count)

def star2():
    with open("input.txt", 'r') as fp:
        
        count = 0
        prev_sum = float('inf')

        depths = [int(x) for x in fp]
        for i in range(len(depths)-2):
            cur_sum = depths[i]+depths[i+1]+depths[i+2]
            if (cur_sum > prev_sum): count += 1
            prev_sum = cur_sum
    
        print(count)



star2()