import math

p2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912]

t = int(input())
for T in range(t):
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    msb = []
    fnl_ans = []
    for i in a:
        if i == 0:
            msb.append(-1)
        else:
            msb.append(int(math.log2(i)))


    allpow = [[0 for i in range(30)] for j in range(n)]
    for i in range(n):
        for j in range(0, 30):
            if i == 0:
                if a[i] ^ p2[j] < a[i]:
                    allpow[i][j] = 1
            else:
                if a[i] ^ p2[j] < a[i]:
                    allpow[i][j] = allpow[i - 1][j] + 1
                else:
                    allpow[i][j] = allpow[i - 1][j]


    notmsb = [[0 for i in range(30)] for j in range(n)]
    for i in range(n):
        for j in range(30):
            if i == 0:
                if a[i] ^ p2[j] < a[i] and msb[i] != j:
                    notmsb[i][j] += 1
            else:
                if a[i] ^ p2[j] < a[i] and msb[i] != j:
                    notmsb[i][j] = notmsb[i - 1][j] + 1
                else:
                    notmsb[i][j] = notmsb[i - 1][j]
                    
    zeros = [0] * n
    for i in range(n):
        if i == 0 and a[i] == 0:
            zeros[i] = 1
        else:
            zeros[i] += zeros[i - 1]
            if a[i] == 0:
                zeros[i] += 1

    
    for Q in range(q):
        l, r = [int(x) - 1 for x in input().split()]

        ans = 0
        if l == 0:
            ans = zeros[r] * (r + 1)
        else:
            ans = (zeros[r] - zeros[l - 1]) * (r - l + 1)
        for i in range(30):
            if l == 0:
                v1 = allpow[r][i]
                v2 = notmsb[r][i]
            else:
                v1 = allpow[r][i] - allpow[l - 1][i]
                v2 = notmsb[r][i] - notmsb[l - 1][i]
##            print(v1, v2)
            ans += v2 * (v1 - v2)
        fnl_ans.append(str(ans))
##        print(ans)
    s = '\n'.join(fnl_ans)
    print(s)
