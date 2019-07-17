n, m = [int(x) for x in input().split()]
s = ''
for i in range(n):
    s += input() + " "
C = s.count("C")
M = s.count("M")
Y = s.count("Y")
if C > 0 or M > 0 or Y > 0:
    print("#Color")
else:
    print("#Black&White")
