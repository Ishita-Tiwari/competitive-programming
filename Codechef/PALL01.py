t = int(input())
for T in range(t):
    s1 = input()
    s2 = s1[::-1]
    if s1 == s2:
        print("wins")
    else:
        print("losses")
