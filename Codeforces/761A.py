a, b = [int(x) for x in input().split()]
n = a + b
diff = a - b
if a == 0 and b == 0:
    print("NO")
elif diff >= -2 and diff <= 2:
    if (n % 2 == 0 and ((a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 !=0)) and (diff <= 1 and diff >= -1)) or (n % 2 !=0 and (a % 2 !=0 or b % 2 != 0)):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
