fact = [1]
for i in range(1, 11):
    fact.append(fact[-1] * i)

s = input()
s1 = input()
n = s.count('+')
n1 = s1.count('+')

if n1 > n:
    print(0) # not possible as both must have equal number of + and -. s1 can't have more
else:
    extra = s1.count('?')
    plus = n - n1
    # how many additional + are required out of 'extra' missing ones?
    # nCr --> out of x, we need to find probablity of getting '+' plus number of times

    c = fact[extra] // (fact[extra - plus] * fact[plus])
    # but we also know that each probablilty is 0.5
    c /= (pow(2, extra))

    print(c)
