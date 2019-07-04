c = 0
total = 0
n = int(input())
for i in range(n):
    s = input()
    c = s.count('1')
    if c > 1:
        total += 1
    c = 0
print(total)
