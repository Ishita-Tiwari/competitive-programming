n = int(input())
s = [0] * n
t = [0] * n
cS = [0] * n
cT = [0] * n
diff = 0
w, l = 0, 0

for i in range(n):
    s[i], t[i] = [int(x) for x in input().split()]
    
    if i == 0:
        cS[i] = s[i]
        cT[i] = t[i]
    else:
        cS[i] = s[i] + cS[i-1]
        cT[i] = t[i] + cT[i-1]
        
    diff = cS[i] - cT[i]
    if diff > 0 and diff > l :
        w = 1
        l = diff
    if diff < 0 and diff * -1 > l:
        w = 2
        l = diff * -1

print(w, l)
