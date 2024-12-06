import re


def check_rule(rule, update):
    nums = rule.split("|")
    num1 = nums[0]
    num2 = nums[1]
    
    pattern = rf'(\b{num1}\b.*\b{num2}\b)'

    # If both numbers are found in order, return True
    if re.search(pattern, update):
        return True
    
    # If either number is missing or they appear in the correct order, return True
    if str(num1) not in update or str(num2) not in update:
        return True

    # If the numbers appear but in the wrong order, return False
    return False

    
def fix_update(rules, update):
    #print(f"\nTesting {update}")
    count = 0
    seq = update.split(",")
    while True:
        start_update = seq.copy()
        for rule in rules:
            if not check_rule(rule, ",".join(seq)):
                nums = rule.split("|")
                r1 = nums[0]
                r2 = nums[1]
                r1_idx = seq.index(r1)
                r2_idx = seq.index(r2)
                r1_item = seq.pop(r1_idx)
                seq.insert(r2_idx, r1_item)
                #print(f"{rule} -> {seq}")

        if start_update == seq:
            return ",".join(seq)
        
        if count > 1000:
            return None
        
        count += 1
       

            

def star1(input):
    sections = input.split("\n\n")
    rules = sections[0].strip().split("\n")
    updates = sections[1].strip().split("\n")
    
    successful_updates = []
    total = 0
    
    for update in updates:
        success = True
        for rule in rules:
            if not check_rule(rule, update):
                success = False
        if success:
            successful_updates.append(update)
    
    for update in successful_updates:
        update_nums = update.split(",")
        middle_idx = len(update_nums)//2
        total += int(update_nums[middle_idx])
        
    return total

def star2(input):
    sections = input.split("\n\n")
    rules = sections[0].strip().split("\n")
    updates = sections[1].strip().split("\n")
    
    updates_to_fix = []
    fixed_updates = []
    total = 0
    
    for update in updates:
        success = True
        for rule in rules:
            if not check_rule(rule, update):
                updates_to_fix.append(update)
                break
            
    
    for update in updates_to_fix:
        fixed_updates.append(fix_update(rules, update))

    for update in fixed_updates:
        update_nums = update.split(",")
        middle_idx = len(update_nums)//2
        total += int(update_nums[middle_idx])
        
    return total
    
    

with open("input.txt") as fp:
    input = fp.read()
    output = star2(input)
    print(output)