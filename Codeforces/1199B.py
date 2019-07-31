h, l = [int(x) for x in input().split()]
print(format((l * l - h * h) / (2 * h), ".13f"))
