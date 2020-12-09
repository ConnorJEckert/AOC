import re

with open("day4_input.txt", 'r') as fp:

    inp = fp.read().split("\n\n")

    valid_count = 0
    
    valid_passport = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    valid_np_creds = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    
    for passport in inp:
        pairs = passport.split()
        codes = set()
        for field in pairs:
            try:
                c = field[0:3]
                data = field[4:]
                print(c + " " + data)
                if (c == "byr"):
                    if (data.isnumeric() and len(data) == 4 and int(data) >= 1920 and int(data) <= 2002):
                        codes.add(c)
                elif (c == "iyr"):
                    if (data.isnumeric() and len(data) == 4 and int(data) >= 2010 and int(data) <= 2020):
                        codes.add(c)
                elif (c == "eyr"):
                    if (data.isnumeric() and len(data) == 4 and int(data) >= 2020 and int(data) <= 2030):
                        codes.add(c)
                elif (c == "hgt"):
                    if (len(data) >= 4):
                        unit = data[-2:]
                        num = int(data[:-2])
                        if (unit == "cm" and num >= 150 and num <= 193):
                            codes.add(c)
                        elif (unit == "in" and num >= 59 and num <= 76):
                            codes.add(c)
                elif (c == "hcl"):
                    if (data[0] == "#" and len(data) == 7):
                        ok_chrs = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8","9"]
                        valid = True
                        for ch in data[1:]:
                            if (ch not in ok_chrs):
                                valid = False
                        if (valid):
                            codes.add(c)
                elif (c == "ecl"):
                    if (len(data) == 3 and data in ["amb","blu","brn","gry","grn","hzl","oth"]):
                        codes.add(c)
                elif (c == "pid"):
                    if (len(data) == 9 and data.isnumeric()):
                        codes.add(c)
            except:
                print('error on ' + c + " " + data)
        if (codes == valid_passport):
            valid_count += 1
        elif (codes == valid_np_creds):
            valid_count += 1
        print(str(codes) +"\n")
        
    print(valid_count)   