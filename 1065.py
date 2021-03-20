def hansu(n):
    counts = 0
    for j in range(1, int(n) + 1):

        j = str(j)
        if len(j) == 1:
            counts += 1

        subtracts = list()
        for i in range(len(j) - 1):

            subtract = int(j[i + 1]) - int(j[i])
            subtracts.append(subtract)

        if len(set(subtracts)) == 1:
            counts += 1

    print(counts)


N = input()
hansu(N)
