n = int(input())
c = 1
rng = int(n ** 0.5) + 1
if n == 1:
    print("Not perfect")
else:
    for i in range(2, rng):
        if n % i == 0:
            c += (i + (n // i))
    if c == n:
        print("Perfect")
    else:
        print("Not Perfect")
