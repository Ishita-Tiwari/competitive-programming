def main():
    t = int(input())
    for T in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        count = []
        from collections import defaultdict as dd
        d = dd(int)
        
        for i in range(n):
            d[a[i]] += 1
 
        l = d.keys()
        for i in l:
            count.append(d[i])
            
        count.sort(reverse = True)
        
        for i in range(len(count) - 1):
            if count[i] <= count[i + 1]:
                count[i + 1] = max(count[i] - 1, 0)
        print(sum(count))
 
main()
