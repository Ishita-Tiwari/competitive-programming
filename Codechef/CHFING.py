for T in range(int(input())):
    n, k = [int(x) for x in input().split()]

    fir = k - 1
    nxt = ((2 * k) - 1) -  (k + n - 1)
    d = fir - nxt

    c = fir + d
    numTerms = c // d

    last = -d * numTerms + c
    ans = (numTerms * (fir + last)) // 2
    
    print(ans % 1000000007)
