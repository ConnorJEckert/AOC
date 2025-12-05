
count = 0

with open("input.txt") as fp:
    lines = fp.read()
    categories = lines.split("\n\n")
    ranges = categories[0].strip()
    ids = categories[1].strip()

    ranges = [x for x in ranges.split("\n")]
    ids = [int(x) for x in ids.split("\n")]

    def check_fresh(ranges, id):
        for r in ranges:
            nums = r.split("-")
            low_n = int(nums[0])
            high_n = int(nums[1])
            if id <= high_n and id >= low_n:
                return True
        return False

    fresh = set()
    not_fresh = set()

    for i in ids:
        if i in fresh or i in not_fresh:
            continue 
        
        if check_fresh(ranges, i):
            fresh.add(i)
        else:
            not_fresh.add(i)

    print(len(fresh))