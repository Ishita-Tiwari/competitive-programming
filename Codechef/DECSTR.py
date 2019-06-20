s = "abcdefghijklmnopqrstuvwxyz"
s = s[::-1]
t = int(input())
for T in range(t):
    k = int(input())
    s1 = ""
    n = k // 25
    n1 = k % 25
    for i in range(n):
        s1 = s + s1
    if n1 > 0:
        s1 = s[-n1 - 1:] + s1
    print(s1)
