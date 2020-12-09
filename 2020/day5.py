import math


def day5_1():
    with open("day5_input.txt", "r") as fp:
        lines = fp.readlines()
        max_seat_id = 0
        for line in lines:
            row = getBinarySelection(line[:7], 127, 0)
            col = getBinarySelection(line[7:], 7, 0)
            seat_id = (row * 8) + col
            max_seat_id = max(seat_id, max_seat_id)
        print(max_seat_id)

def day5_2():
    with open("day5_input.txt", "r") as fp:
        lines = fp.readlines()
        taken_seats = set()
        for line in lines:
            row = getBinarySelection(line[:7], 127, 0)
            col = getBinarySelection(line[7:], 7, 0)
            seat_id = (row * 8) + col
            taken_seats.add(seat_id)
        
        full_seats = set([item for item in range(0, 891)])
        missing_seats = full_seats - taken_seats
        print("missing seats: " + str(missing_seats))


def getBinarySelection(inText, mx, mn):
    max_n = mx
    min_n = mn
    for letter in inText:
        if (letter == "L" or letter == "F"):
            half = math.ceil((max_n-min_n)/2)
            max_n = max_n - half
        elif (letter == "R" or letter == "B"):
            half = math.ceil((max_n-min_n)/2)
            min_n = min_n + half
    if (max_n == min_n):
        return max_n
    else:
        return -1




day5_2()