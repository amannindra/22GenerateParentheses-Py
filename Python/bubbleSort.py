def bubbleSort(array):
    for j in range(len(array)):
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
        print(array)
    return array


bubbleSort([8,7,6,5,4,3,2,1])
print("--------------------------------")
bubbleSort([1,2,3,4,5,6,7,8,9])
