n = int(input())
num = n + 1
ans = 0
if n < 987654321:
    while(True):
        n1 = str(num)
        l = list(n1)
        if '0' in l:
            num += 1
            continue
        s = set(n1)
        if n1.count('0') == 0 and len(l) == len(s):
            ans = num
            break
        num += 1
print(ans)
