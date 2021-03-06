a = input()
b = input()
c = input()

s = int(a) * int(b) * int(c)

d = dict()

for i in range(10):
    d[str(i)] = 0

for i in range(len(str(s))):
    d[str(s)[i]] += 1

for val in d.values():
    print(val)
