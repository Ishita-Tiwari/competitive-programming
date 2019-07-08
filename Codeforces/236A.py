s = input()
l = list(s)
c = [0] * 26
count = 0
for i in range(len(s)):
    c[ord(l[i]) - 97] += 1
for i in range(26):
    if c[i] > 0:
        count += 1
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
