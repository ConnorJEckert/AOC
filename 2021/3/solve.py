
def common_bit(index, lines):
    bits = [x[index] for x in lines]
    common = '0'
    if (bits.count('0') > bits.count('1')):
        common = '1'
    return common

def prune_list(index, bit, lines):
    output = []
    for num in lines:
        if num[index] == bit:
            output.append(num)
    return output

def star1():
    with open("input.txt") as fp:
        gamma = ''
        lines = fp.read().splitlines()
        for i in range(len(lines[0])):
            gamma += common_bit(i, lines)
        gamma = int(gamma, 2)
        epsilon = 0b111111111111 - gamma
        
        print(gamma*epsilon)

def star2():
    with open("input.txt") as fp:
        oxy_rating = fp.read().splitlines()
        co2_rating = oxy_rating.copy()

        for i in range(12):
            if (len(oxy_rating) == 1):
                break
            common = common_bit(i, oxy_rating)
            oxy_rating = prune_list(i, common, oxy_rating)

        for i in range(12):
            if (len(co2_rating) == 1):
                break
            common = common_bit(i, co2_rating)
            rare = "0"
            if(common_bit(i, co2_rating) == "0"):
                rare = "1"
            co2_rating = prune_list(i, rare, co2_rating)

        print(int(oxy_rating[0],2) * int(co2_rating[0],2))
    

star2()