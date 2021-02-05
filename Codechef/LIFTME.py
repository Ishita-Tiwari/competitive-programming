t = int(input())
for T in range(t):
    n, q = [int(x) for x in input().split()]
    ans = 0
    move = [0]
    for Q in range(q):
        f, d = [int(x) for x in input().split()]
        move.append(f)
        move.append(d)

    for i in range(1, len(move)):
        ans += abs(move[i] - move[i - 1])
    print(ans)
