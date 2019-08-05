def count(s1, E, O):
    c = 0
    for i in s1:
        num = i
        c = 0
        while(num):
            c += num & 1
            num >>= 1

        if c % 2 == 0:
            E += 1
        else:
            O += 1
    print(E, O)
    return(E, O)

def main():
    t = int(input())
    for T in range(t):
        s, s1 = set(), set()
        q = int(input())
        l = []
        E, O = 0, 0
        for i in range(q):
            s1 = set()
            val = int(input())

            
            if val not in s:
                s.add(val)
                s1.add(val)
                for j in s:
                    if j != val:
                        l.append(val ^ j)
                for j in l:
                    if j not in s:
                        s1.add(j)
                    s.add(j)
                l = []
            E, O = count(s1, E, O)

main()
