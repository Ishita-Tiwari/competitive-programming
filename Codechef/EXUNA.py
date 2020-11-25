t = int(input())
for T in range(t):
	n = int(input())
	l = [int(x) for x in input().split()]
	for i in range(1, n):
		l[0] %= l[i]
	print(l[0])
