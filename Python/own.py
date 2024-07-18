def substrings(s):
    l = []
    for i in range(len(s)):
        word = ""
        word += s[i]

        for j in range(i + 1,len(s)):
            word += s[j]
            l.append(word)
    print(l)
            

substrings("abcdefg")
    