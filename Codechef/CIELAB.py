a, b = [int(x) for x in input().split()]
diff = a - b
n = len(str(diff))
if diff % 10 != 9:
    print(diff + 1)
else:
    print(diff - 1)
