from math import ceil
n, m = [int(x) for x in input().split()]

# case 1: all of them have 1 person. last team has the rest --> max
rem = n - m + 1
mx = rem * (rem - 1) // 2

# case 2: evenly distributed people --> min
rem -= 1 # extra left after assigning minimum equal to teams

# floor value and having ceil value
lsval = n // m
gtval = 0
if n % m > 0:
    gtval = lsval + 1
# number of teams having the floor and ceil value
gtnum = n % m
lsnum = m - gtnum

##print(lsnum, lsval, gtnum, gtval)

mn = lsnum * ((lsval * (lsval - 1)) // 2)
mn += gtnum * ((gtval * (gtval - 1)) // 2)

print(mn, mx)
