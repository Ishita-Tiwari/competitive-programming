power = []
val = 1
while(val < 1000000000):
    power.append(val)
    val *= 2
power.append(val)

t = int(input())
for T in range(t):
    n = int(input())
    bn = bin(n)[2:]
    if bn.count('1') == 1:
        print(-1)
        continue

    ans = 0
    for i in range(len(power)):
        if power[i] > n:
            break
        ans += power[i] * ((n + power[i]) // (2 * power[i]))
    print(ans - 1)
