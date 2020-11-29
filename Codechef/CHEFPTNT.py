t=int(raw_input())
for _ in range(t):
	n, m, x, k = [int(x) for x in raw_input().split()]
	month = raw_input()
	if x * m < n:
		print "no"
	else:
		even = month.count('E')
		odd = month.count('O')
		poss = 0
		for i in range(1, m + 1):
			if i % 2 == 1:
				if odd > 0:
					poss += min(x, odd)
					odd -= min(x, odd)
					
			else:
				if even > 0:
					poss += min(x,even)
					even -= min(x,even)
					
		if poss >= n:
			print "yes"
		else:
			print "no" 
