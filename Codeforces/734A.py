n = int(input())
s = input()
A = s.count("A")
D = s.count("D")
if A == D:
    print("Friendship")
elif A > D:
    print("Anton")
else:
    print("Danik")
