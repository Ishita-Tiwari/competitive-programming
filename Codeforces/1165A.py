n, x, y = [int(x) for x in input().split()]
num = input()
nx = num[-x :]
c = 0
ny = "1" + "0" * y
mul = '0'  * (len(nx) - len(ny))
ny = mul + ny
for i, j in zip(nx, ny):
    if i != j:
        c += 1
print(c)
