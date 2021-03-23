import string

S = input()

# making dict of alphabet ( default is -1 )
d = dict.fromkeys(string.ascii_lowercase, -1)

for i in range(len(S)):
    
    if d[S[i]] == -1:  # Only when it first appears
        d[S[i]] = i

value_list = d.values()
for i in value_list:
    print(i, end=' ')
