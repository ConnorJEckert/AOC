def star1():
    with open("input.txt", 'r') as fp:
      total = 0
      input = input.split("\n")
      list1 = []
      list2 = []
      for indx in range(len(input)):
          pair = input[indx].split()
          if pair:
              list1.append(pair[0])
              list2.append(pair[1])
              
      list1.sort()
      list2.sort()
      
      for indx in range(len(list1)):
          diff = abs(int(list1[indx]) - int(list2[indx]))
          total += diff
      
      print(total)

def star2():
    with open("input.txt", 'r') as fp:
      total = 0
      input = input.split("\n")
      list1 = []
      list2 = []
      for indx in range(len(input)):
          pair = input[indx].split()
          if pair:
              list1.append(pair[0])
              list2.append(pair[1])
              
      list1.sort()
      list2.sort()
      
      for indx in range(len(list1)):
          num = list1[indx]
          c = list2.count(num)
          sim = int(num)*c
          total += sim
      
      print(total)



