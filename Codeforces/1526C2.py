from heapq import heapify, heappush, heappop

n = int(input())
l = [int(x) for x in input().split()]
count = 0
sm = 0
mn = []
heapify(mn)

for i in range(n):
    sm += l[i]
    count += 1
    if l[i] < 0:
        heappush(mn, l[i])
    if sm < 0:
        sm -= heappop(mn)
        count -= 1

print(count)
