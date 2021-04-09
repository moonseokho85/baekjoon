word = input()

croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0

for i in range(len(word)):
    if word[i:i+2] in croatia_alphabet:
        word.replace(word[i:i+2], '')
        count += 1
        if word[i:i+3] in croatia_alphabet:
            word.replace(word[i:i+3], '')
            count += 1

print(count + int(len(word)))