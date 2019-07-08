c = 0
n = int(input())
s = input()
l = s
for i in range(n-1):
    if l[i] == l[i+1]:
        c += 1
print(c)
