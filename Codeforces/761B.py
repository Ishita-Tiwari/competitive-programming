n, L = [int(x) for x in input().split()]
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
d1 = [0] * n
d2 = [0] * 2 *n
s1, s2 = 0, 0
st1, st2 = '', ''
for i in range(n-1):
    d1[i] = l1[i+1] - l1[i]
    d2[i] = l2[i+1] - l2[i]
    s1 += d1[i]
    s2 += d2[i]
d1[n-1] = L - s1
d2[n-1] = L - s2
 
for i in range(n):
    d2[i+n] = d2[i]
    st1 += str(d1[i])
for i in range(2 * n):
    st2 += str(d2[i])
 
if st1 in st2:
    print("YES")
else:
    print("NO")
