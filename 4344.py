test_case_count = input()

for i in range(int(test_case_count)):
    test_case = input()

    # spliting string to list
    test_case = test_case.split()

    # converting each string to int
    test_case = [int(i) for i in test_case]

    student_count = test_case[0]
    scores = test_case[1:]

    sum_of_scores = sum(scores)
    mean = sum_of_scores / student_count

    counts = 0
    for j in scores:
        if j > mean:
            counts += 1

    proportion = (counts / student_count) * 100
    proportion = round(proportion, 3)
    print('%.3f' % proportion + '%')
