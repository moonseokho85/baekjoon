# Function of hansu
def hansu(n):
    counts = 0
    for j in range(1, int(n) + 1):

        # Stringify input number
        j = str(j)

        # If input number is one digit, count it
        if len(j) == 1:
            counts += 1

        subtracts = list()
        for i in range(len(j) - 1):

            # Judge the isometric sequence
            subtract = int(j[i + 1]) - int(j[i])
            subtracts.append(subtract)

        if len(set(subtracts)) == 1:
            counts += 1

    print(counts)


# Input number
N = input()

# Calculate of input number through function of hansu
hansu(N)
