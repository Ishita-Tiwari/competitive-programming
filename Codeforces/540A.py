n = int(input())
s1 = input()
s2 = input()
ans = 0
 
for i in range(n):
    diff = abs(int(s1[i]) - int(s2[i]))
    if diff > 4:
        diff = 10 - diff
    ans += diff
print(ans)
