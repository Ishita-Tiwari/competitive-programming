n = int(input())
a = [int(c) for c in input().split()]
 
l = [0] * 4
for i in a:
    l[i - 1] += 1
one, two, three, four = l
 
sub = min(one, three)
ans = four + sub + (two // 2)
 
three -= sub
one -= sub
two -= ((two // 2) * 2)
 
ans += three
sub = min(one // 2, two)
ans += sub
 
two -= sub
one -= (2 * sub)
 
if two:
    ans += 1
elif one:
    ans += (one // 4) + (one % 4 >= 1)
print(ans)
