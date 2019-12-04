
def part1():
	two_count = 0
	three_count = 0

	for line in open("day2_input.txt",'r'):
		tw = False
		th = False
		for c in line:
			if (line.count(c) == 2):
				tw = True
			if (line.count(c) == 3):
				th = True
		if (tw):
			two_count += 1 
		if (th):
			three_count += 1

	print("two:" + str(two_count))
	print("three:" + str(three_count))
	print("sum: " + str(two_count * three_count))



def part2():

	def check_diff(word1, word2):
		same = ""
		for i in range(26):
			if (word1[i] == word2[i]):
				same += word1[i]
		return same

	
	words = []
	for word in open("day2_input.txt",'r'):
		words.append(word[:-2])

	while True:
		word1 = words[0]
		for word2 in words[1:]:
			if len(word2) == 0:
				return
			same = check_diff(word1, word2)
			if (len(same) == 25):
				print(same)
				return
		words.remove(word1)
		if (len(words) == 0):
			print("end of list")
			return



part2()

