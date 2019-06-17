n = int(input())
a = input()
a = a.replace(" ", "")
l = list(a)
a = ''
l.sort(reverse = True)
for i in l:
    a += i
print(a)
