def loop(ans, v1, v2, a, n, i):
    for j in range(i + 1, n):
        v1 ^= a[j]
        v2 = a[j]
        for k in range(j, n):
            v2 ^= a[k]
            if v1 == v2 and i < j and j <= k:
                ans += 1
    return(ans)


def cal(a, n):
    ans, v1, v2 = 0, 0, 0

    for i in range(n):
        v1 = a[i]
        ans = loop(ans, v1, v2, a, n, i)
##        for j in range(i + 1, n):
##            v1 ^= a[j]
##            v2 = a[j]
##            for k in range(j, n):
##                v2 ^= a[k]
##                if v1 == v2 and i < j and j <= k:
##                    ans += 1
    print(ans)


def main():
    t = int(input())
    for T in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        ans = cal(a, n)
main()
