from collections import defaultdict as dd

 

for i in range(int(input())):

    n, m = [int(x) for x in input().split()]

    arr = []

 

    for i in range(n):

        a = [int(x) for x in input().split()]

        arr.append(a)

 

    d = dd(int)

    lis = []

    for i in range(n):

        for j in range(m):

            lis.append(arr[i][j])

 

    lis = sorted(lis)

 

    ans = [[0 for i in range(m)] for j in range(n)]

 

    pos = 0

    vert = 0

   

    if m % 2 == 0:

 

        while(vert < m // 2):

            for i in range(n):

                ans[i][vert] = lis[pos]

                pos += 1

                ans[i][m - vert - 1] = lis[pos]

                pos += 1

            vert += 1

    else:

        from collections import defaultdict as dd

        d = dd(int)

        odd = []

        new = []

       

        for i in lis:

            d[i] += 1

 

        for i in d.keys():

            if d[i] % 2 == 0:

                for j in range(d[i]):

                    new.append(i)

            else:

                cnt = d[i]

                while(cnt > 1):

                    new.append(i)

                    cnt -= 1

                odd.append(i)

 

        if len(odd) > n:

            print(-1)

            continue

       

            

            

        while(vert < m // 2):

            for i in range(n):                   

                ans[i][vert] = new[pos]

                pos += 1

                ans[i][m - vert - 1] = new[pos]

                pos += 1

            vert += 1

 

        tt = 0

 

        if len(odd) >= n:

            for i in range(n):

                ans[i][m // 2] = odd[tt]

                tt += 1

        else:

            for i in range(len(odd)):

                ans[i][m // 2] = odd[tt]

                tt += 1

 

            for i in range(len(odd), n):

                ans[i][m // 2] = new[pos]

                pos += 1

 

    bad = 0

    for i in range(n):

        if ans[i] != ans[i][::-1]:

            bad = 1

            break

    if bad:

        print(-1)

    else:

        for i in ans:

            print(*i)
