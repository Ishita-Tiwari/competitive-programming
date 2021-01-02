m = int(input())
a = [int(x) for x in input().split()]
n = int(input())
for N in range(n):
    ind = int(input()) - 1
    print(a.pop(ind))
