x = 0
n = int(input())
while(n > 0):
    s = input()
    if s.count('+') > 0:
        x += 1
    if s.count('-') > 0:
        x -= 1
    n -= 1
print(x)
