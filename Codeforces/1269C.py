from math import ceil
n, k = [int(x) for x in input().split()]
x = input()
s1 = x[:k]
ans = s1 * (ceil(n / k))
ans = ans[:n]

if int(ans) < int(x):
    ans = ""
    s1 = str(int(s1) + 1)
    ans = s1 * (ceil(n / k))
    ans = ans[:n]

print(len(ans))
print(ans)
    
    
