from itertools import groupby


def part1():

	def check_num(num):
		str_num = str(num)
		double = False
		for i in range(5):
			if (str_num[i] > str_num[i+1]):
				return False
			if (str_num[i] == str_num[i+1]):
				double = True
		return double

	count = 0
	for i in range(273025, 767253+1):
		 if (check_num(i)):
		 	count += 1
	print(count)



def part2():

	def check_ascd(num):
		str_num = str(num)
		for i in range(5):
			if (str_num[i] > str_num[i+1]):
				return False
		return True

	def check_doubles(num):
		groups = ["".join(grp) for num, grp in groupby(str(num))]
		for group in groups:
			size = len(group)
			if (size == 2):
				return True
		return False

	count = 0
	for i in range(273025, 767253+1):
		 if (check_ascd(i) and check_doubles(i)):
		 	count += 1
	print(count)



part2()



"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle answer was 910.

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle answer was 598.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your Advent calendar and try another puzzle.

Your puzzle input was 273025-767253.
"""