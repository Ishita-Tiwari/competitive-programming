s = input()
if s[0:1].isupper() == False:
    s = s[0:1].upper() + s[1:len(s)]
print(s)
