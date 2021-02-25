t = int(input())
for T in range(t):
    n = int(input())
    h = [int(x) for x in input().split()]

    can_move = 0
    if h[0] > 0:
        can_move = h[0]
    ans = 'YES'

    for i in range(1, n):
##        print(h[i] + can_move)
        if h[i] + can_move < i:
            ans = 'NO'
            break
        can_move += h[i] - i
        

    print(ans)
