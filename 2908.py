two_constant = input()

# Spliting two constants
constants = two_constant.split(' ')

# Making reversed constants list
reversed_constants = list()
for i in range(len(constants)):

    # Calculating length of the list
    string_length = len(constants[i])

    # Slicing
    sliced_string = constants[i][string_length::-1]
    reversed_constants.append(sliced_string)

# Printing max value of the reversed constants
print(max(reversed_constants))
