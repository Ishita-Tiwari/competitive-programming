prof = 0
t = int(input())
for T in range(t):
    num = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    n = int(input())
    if n == 0:
        print("-400")
        prof -= 400
        continue
    mx = -400
    for N in range(n):
        inp = [x for x in input().split()]
        num[ord(inp[0]) - 65][int(inp[1]) // 3 % 4] += 1

    f = 3 ^ 2 ^ 1 ^ 0
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            for k in range(4):
                if i == k or j == k:
                    continue
                a = [0, 0, 0, 0]
                l = f ^ i ^ j ^ k
                a[0] = num[0][i]
                a[1] = num[1][j]
                a[2] = num[2][k]
                a[3] = num[3][l]
                a.sort()
                val = 0
                c = 4
                for x in range(3, -1, -1):
                    if a[x] != 0:
                        val += c * 25 * a[x]
                        c -= 1
                    else:
                        val -= 100
                mx = max(mx, val)
    print(mx)
    prof += mx
print(prof)
