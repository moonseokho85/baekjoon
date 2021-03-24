import string

# Making dictionary of alphabet order
d = dict.fromkeys(string.ascii_uppercase, 0)

word = input()

# Converting uppercase if word is lowercase
word = word.upper()
for i in range(len(word)):
    d[word[i]] += 1

# Extracting max value in alphabet dictionary
d_max_value = max(d.values())

# Extracting keys related to max value
d_max_keys = list()
for key, value in d.items():
    if value == d_max_value:
        d_max_keys.append(key)

if len(d_max_keys) != 1:
    print("?")
else: 
    print(d_max_keys[0])