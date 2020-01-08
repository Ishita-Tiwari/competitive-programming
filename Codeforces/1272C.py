n, alpha = [int(x) for x in input().split()]
s = input()
l = [x for x in input().split()]
mark = [0] * n
st = set(l)
count = 0
val = 0
for i in range(n):
    if s[i] not in st:
        mark[i] = val
        val = 0
    else:
        val += 1
if val > 0:
    count += (val * (val + 1)) // 2
##print(count)
for i in range(n):
    if mark[i] != 0:
        count += (mark[i] * (mark[i] + 1)) // 2
##        print(count)
        
print(count)
