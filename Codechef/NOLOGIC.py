t = int(input())
s = "abcdefghijklmnnopqrstuvwxyz"
for T in range(t):
    n = input()
    n = n.lower()
    ans = ""
    c = 0
    for i in s:
        if i not in n:
            ans += i
            c = 1
    if c == 1:
        print(ans)
    else:
        print("~")
