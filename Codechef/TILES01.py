n = int(input())
l = [1, 0]

for N in range(n):
    l[0], l[1] = sum(l) % 15746, l[0] % 15746
print(l[0])
