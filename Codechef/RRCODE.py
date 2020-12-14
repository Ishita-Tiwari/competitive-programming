def fnc(n, k, answer, s, a):
    for i in range(k):
        for j in range(n):
            if s == "XOR": answer ^= a[j]
            elif s == "OR": answer |= a[j]
            else: answer &= a[j]
        
    return(answer)


t = int(input())
for T in range(t):
    n, k, answer = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    s = input().strip()
    if s == "XOR": k %= 2
    else: k = min(k, 1)
    print(fnc(n, k, answer, s, a))
