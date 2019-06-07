n = int(input())
x = int(input(), 2)
c = 0
for i in range(100000):
    if x % (2 ** i) != 0:
        c = i - 1
        break
print(c)
