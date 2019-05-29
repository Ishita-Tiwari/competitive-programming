x, y = [float(x) for x in input().split()]
if x % 5 == 0 and x + 0.50 <= y:
    balance = y - x - 0.50
    print("{:.2f}".format(balance))
else:
    print("{:.2f}".format(y))
