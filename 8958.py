test_case_count = input()

for i in range(int(test_case_count)):
    ox_result = input()

    # string to list
    ox_result = list(ox_result)

    point = 0
    points = list()
    for i in ox_result:
        if i == 'O':
            point += 1
            points.append(point)
        else:
            point = 0

    print(sum(points))