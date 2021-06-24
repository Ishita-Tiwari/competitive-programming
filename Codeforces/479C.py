n = int(input())
val = []
a, b = [], []
for i in range(n):
    val.append([int(x) for x in input().split()])
    a.append(val[i][0])
    b.append(val[i][1])

# sorting as per 'a' and then 'b' as 'a' will be noted in the record
val.sort()

# have to start with the exam on the smallest a (but take it on b). in this, if there are multiple
# options, then we start with the smallest b in them.

day = val[0][1]
for i in range(1, n):
##    print(day)
    if val[i][1] >= day:
        day = val[i][1]
    else:
        day = val[i][0]
##    print(day, '\n\n')
print(day)
