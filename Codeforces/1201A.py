n, m = [int(x) for x in input().split()]
op = []
for N in range(n):
    op.append(list(input()))
a = [int(x) for x in input().split()]
s, ans = '', 0
for i in range(m):
    val = 0
    s = ''
    for j in range(n):
        s += op[j][i]
    #print(s)
    val = max(val, a[i] * max(s.count('A'), s.count('B'), s.count('C'), s.count('D'), s.count('E')))
    ans += val
print(ans)
