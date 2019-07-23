a, b = [int(x) for x in input().split()]
years = 1
while(True):
    a *= 3
    b *= 2
    if a > b:
        break
    years += 1
print(years)
