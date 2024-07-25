def SelectionSort(array):
    for i in range(len(array)):
        minindex = i
        for j in range(i + 1, len(array)):
            if array[minindex] > array[j]:
                minindex = j
        temp = array[i]
        array[i] = array[minindex]
        array[minindex] = temp
        print(array)

    return array


# print(SelectionSort([8, 7, 6, 5, 4, 3, 2, 1]))


def merge(a, b):
    c = []
    i = 0
    j = 0
    count = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        
        elif a[i] > b[j]:
            c.append(b[i])
            j += 1
        count += 1

    if (i == len(a)):
        while j < len(b):
            c.append(b[j])
            j += 1
            count += 1
    else:
        while i < len(a):
            c.append(a[i])
            i += 1
            count += 1
    return c


a = [1, 3,6, 8]
b = [2, 2, 4, 5,  5, 6, 8]
c = []

print(merge(a, b))
