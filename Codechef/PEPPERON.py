t = int(input())
for T in range(t):
    n = int(input())
    mid = n // 2
    l1 = []
    l2 = []
    val = []
    for i in range(n):
        num = input()
        s1 = num[:mid]
        s2 = num[mid:]
        l1.append(s1.count('1'))
        l2.append(s2.count('1'))
    v1 = sum(l1)
    v2 = sum(l2)
    diff = abs(v1 - v2)
    for i in range(n):
        diff = min(diff, abs((v1 - l1[i] + l2[i]) - (v2 - l2[i] + l1[i])))
    print(diff)
