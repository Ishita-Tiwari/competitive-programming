def gcd(a, b):
    if a == 0:
        return b
    return(gcd(b % a, a))

def calc(g, n):
    count = 0
    val = 1
    while(val ** 2 <= g):
        if g % val == 0:
            if val <= n:
                count = max(count, val)
            if g // val <= n:
                count = max(count, g // val)
        val += 1
    return count


t = int(input())
for T in range(t):
    n, m = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    if n == 1:
        print(0)
        continue

    g = p[0]
    for i in p:
        g = gcd(g, i)

    ans = n
    ans -= calc(g, n)

    print(ans)
