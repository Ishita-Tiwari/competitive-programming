t = int(input())
for T in range(t):
    s = input()
    val = ""
    count = 0
    word = ["c", "e", "f", "h"]
    for i in range(len(s)):
        val = s[i:i + 4]
        l = list(val)
        l.sort()
        if l == word:
            count += 1
    
    if count == 0:
        print("normal")
    else:
        print("lovely", count)
