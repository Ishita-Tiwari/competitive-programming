def cal(s, n, one):
    for i in range(n):
        if s[i] == '1':
            if i - 1 >= 0 and s[i - 1] != '.':
                s[i - 1] = str(abs(int(s[i - 1]) - 1))
                if s[i - 1] == '1':
                    one += 1
                else:
                    one -= 1
            if i + 1 < n and s[i + 1] != '.':
                s[i + 1] = str(abs(int(s[i + 1]) - 1))
                if s[i + 1] == '1':
                    one += 1
                else:
                    one -= 1
            s[i] = '.'
            one -= 1
    return(s, one)
def main():
    t = int(input())
    for T in range(t):
        s = list(input())
        one = s.count('1')
        n = len(s)
        c = 0
        while(one > 0):
            s, one = cal(s, n, one)
        for i in range(n):
            if s[i] == '0':
                c = -1
                break
        if c == -1:
            print("LOSE")
        else:
            print("WIN")

main()
