import string

word = input()

# Making alphabet key dictionary
d = dict.fromkeys(string.ascii_uppercase, 0)

for index, key in enumerate(d):
    for i in range(2, 10):
        d[key] = i

print('d:', d)