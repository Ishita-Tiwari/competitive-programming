t = int(input())
for T in range(t):
    s = input()
    hsh = [0] * 26
    n = len(s)
    odd = 0
    for i in range(n):
        hsh[ord(s[i]) - 97] += 1
    for i in hsh:
        if i % 2 == 1:
            odd += 1
    if n % 2 == 0:
        if odd == 2:
            print("DPS")
        else:
            print("!DPS")
    else:
        if odd == 1 or odd == 3:
            print("DPS")
        else:
            print("!DPS")
            
