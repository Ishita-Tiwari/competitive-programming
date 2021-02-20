from sys import stdin, stdout
n = 1000005
prime = [1 for i in range(n + 1)]
p = 2
while(p * p <= n):
    if prime[p]:
        for i in range(p * p, n + 1, p):
            prime[i] = 0
    p += 1

prm = [0, 0]
for i in range(2, n):
    prm.append(prime[i])
for i in range(1, n):
    prm[i] = prm[i] + prm[i - 1]
            

t = int(stdin.readline())
for T in range(t):
    x, y = [int(x) for x in stdin.readline().split()]
    if y < prm[x]:
        print("Divyam")
    else:
        print("Chef")
