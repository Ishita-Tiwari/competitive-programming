pwr = [1]
val = pow(10, 18)
x = 1
while(pwr[-1] < val):
    pwr.append(pow(2, x))
    x += 1
t = int(input())
for T in range(t):
    x = int(input())
    ans = 1
    for i in pwr:
        if i < x:
            ans = i
        else:
            ans = i
            break
    print(ans)
