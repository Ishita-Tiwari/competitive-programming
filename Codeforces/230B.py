p = 2
prime = [True for i in range(1000001)]
while(p * p < 1000001):
    if prime[p]:
        for i in range(p * 2, 1000001, p):
            prime[i] = False
    p += 1
primeSet = set()
for i in range(2, len(prime)):
    if prime[i]:
        primeSet.add(i)

        

def isTPrime(n):
    if int(n ** 0.5) != n ** 0.5:
        return 0
    if int(n ** 0.5) in primeSet:
        return 1
    return 0

n = int(input())
l = [int(x) for x in input().split()]

for i in l:
    if isTPrime(i):
        print('YES')
    else:
        print('NO')

