l = [1] * 1000005
for i in range(1, 1000005):
    l[i] = (i * l[i-1]) % 1000000007

t = int(input())
for T in range(t):
    n = int(input())
    print(l[n+1] - 1)
