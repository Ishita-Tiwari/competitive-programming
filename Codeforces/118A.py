s = input().lower()
vow = 'aoyeui'
S = ''
for letter in vow:
    s = s.replace(letter, '')
for letter in s:
    S += ".%s" % letter
print(S)
