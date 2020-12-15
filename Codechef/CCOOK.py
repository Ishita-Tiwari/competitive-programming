t = int(input())
for T in range(t):
    l = [int(x) for x in input().split()]
    ans = ["Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean"]
    print(ans[l.count(1)])
