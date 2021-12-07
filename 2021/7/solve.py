import numpy as np


def sumFactorial(i):
    sum = 0
    while i>0:
        sum += i
        i -= 1
    return sum

def calcCost(positions, x):
    total_cost = 0
    for pos in positions:
        total_cost += abs(x-pos)
    return total_cost

def calcCost2(positions, x):
    total_cost = 0
    for pos in positions:
        total_cost += sumFactorial(abs(x-pos))
    return total_cost


def star1():
    with open("input.txt") as fp:
        best_cost = float('inf')
        positions = [int(x) for x in fp.readline().strip().split(",")]
        max_position = max(positions)
        min_position = min(positions)
        for x in range(min_position, max_position+1):
            cost = calcCost(positions, x)
            if (cost < best_cost):
                best_cost = cost
        print(best_cost)

def star2():
    with open("input.txt") as fp:
        best_cost = float('inf')
        positions = [int(x) for x in fp.readline().strip().split(",")]
        max_position = max(positions)
        min_position = min(positions)
        for x in range(min_position, max_position+1):
            cost = calcCost2(positions, x)
            if (cost < best_cost):
                best_cost = cost
        print(best_cost)



star2()