string = input()

# Spliting string based on spacing
string = string.split(' ')

words = list()
for i in range(len(string)):
    if len(string[i]) != 0:
        words.append(string[i])

# Printing length of list
print(len(words))