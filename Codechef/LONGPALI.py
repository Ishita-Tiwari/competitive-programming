def palid(s):
    for i in range(int(len(s)/2)):
        j=int(len(s)-1-i)
        if s[i]!=s[j]:
            return False
    return True


t=int(input())
s=input()
max=""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if palid(s[i:j]):
            if len(max)<len(s[i:j]):
                max=s[i:j]
print(len(max))
print(max)
