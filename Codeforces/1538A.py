t = int(input())
for T in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    mn, mx = min(a), max(a)

    indmn, indmx = a.index(mn), a.index(mx)

    case1, case2, case3 = 0, 0, 0
    case1 = max(indmn, indmx) + 1
    case2 = n - min(indmn, indmx)
    case3 = min(indmn, indmx) + 1 + n - max(indmn, indmx)

    print(min(case1, case2, case3))
