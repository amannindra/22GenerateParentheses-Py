b = ["b", "c", "a", "f", "q", "c", "a", "f", "b", "d", "l", "v"];

def occurrence(l1):
    a = set()
    s = []
    for i in range(len(b)):
        # print(s[i][0])
        if b[i] not in a:
            s.append([b[i], i])
            a.add(b[i])
    f = set()
    j = []
    for i in range(len(b) - 1, -1, -1):
        # print(s[i][0])
        if b[i] not in f:
            j.append([b[i], i])
            f.add(b[i])
    return [s,j]


print(occurrence(b)[0])
print(occurrence(b)[1])
        
    
    