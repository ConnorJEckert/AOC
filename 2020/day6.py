

with open("day6_input.txt", "r") as fp:
    lines = fp.read()
    groups = lines.split("\n\n")
    total_count = 0
    for group in groups:
        individuals = group.split("\n")
        ind_answers = []
        for ind in individuals:
            answers = set()
            for letter in ind:
                answers.add(letter)
            ind_answers.append(answers)
        com_ans = ind_answers[0]
        for s in ind_answers:
            com_ans = com_ans.intersection(s)
        total_count += len(com_ans)
    print(total_count)
   
    