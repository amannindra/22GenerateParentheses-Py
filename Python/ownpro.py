def sums(l1, l2):
    l = []
    for i in range(len(l2)):
        k = 0
        for j in range(l2[i][0], l2[i][1] + 1):
            k += l1[j]
        l.append(k)
    print(l)
    return l


def sums2(l1, l2):
    l = []
    c = 0
    for i in range(len(l1)):
        c += l1[i]
        l.append(c)
    print(l)
    j = []
    for i in range(len(l2)):
        left = l2[i][0]
        right = l2[i][1]
        if left == 0:
            j.append(l[right])
        else:
            j.append(l[right] - l[left - 1])
    return j


l1 = [2, 5, 7, 9, 3, 8]
l2 = [[2, 4], [1, 5], [0, 3]]
# print(sums(l1, l2))
print(sums2(l1, l2))
