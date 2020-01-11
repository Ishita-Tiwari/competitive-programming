n = int(input())
one = "I hate that "
two = "I love that "
s = ""
ans = ""
if n % 2 == 0:
    s = "I love it"
else:
    s = "I hate it"
for i in range(1, n):
    if i % 2 == 0:
        ans += two
    else:
        ans += one
ans += s
print(ans)
