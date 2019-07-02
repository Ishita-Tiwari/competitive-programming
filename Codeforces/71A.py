n = int(input())
while(n > 0):
    w = input()
    l = len(w)
    if l <= 10:
        print(w)
    else:
        w = w[0:1] + str(l-2) + (w[l-1:l])
        print(w)
    n -= 1
