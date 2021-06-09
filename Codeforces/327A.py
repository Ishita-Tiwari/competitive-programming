n = int(input())
l = [int(x) for x in input().split()]
c1, c0 = 0, 0
inc = 0
mx = 0
total1 = sum(l)

for i in range(n):
    c1, c0 = 0, 0
    for j in range(i, n):
        c1 += l[j]
        c0 += (1 - l[j])
        inc = c0
        mx = max(mx, inc + total1 - c1)

print(mx)
        
