t = int(input())
for T in range(t):
    n, k = [int(x) for x in input().split()]
    s = list(input())
 
    l = ['1'] * n
    ind = 0
    for i in range(n):
        if s[i] == '0':
            val = min(k, i - ind)
            k -= val
            l[i - val] = '0'
            ind += 1
            
    print("".join(l))
