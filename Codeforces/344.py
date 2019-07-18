n = int(input())
s = ''
for i in range(n):
    s += input()
print(s.count("00") + s.count("11") + 1)
