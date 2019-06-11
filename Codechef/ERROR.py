t = int(input())
for T in range(t):
    s = input()
    g1 = "010"
    g2 = "101"
    if g1 in s or g2 in s:
        print("Good")
    else:
        print("Bad")
