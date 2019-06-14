while(True):
    n = int(input())
    if n == 0:
        break
    else:
        c = 0
        l = [int(x) for x in input().split()]
        l.sort(reverse = True)
        for i in range(0, n):
            j = i + 1
            k = n - 1
            while j < k:
                if l[j] + l[k] < l[i]:
                    c += k - j
                    k -= 1
                else:
                    j += 1
        print(c)
