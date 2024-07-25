array = [1, 2, 4, 5, 6, 7, 5, 7]


print(array)

# for i in range(len(array)):
#     print(array[-i-1], array[-1])
#     if array[-i-1] != array[-1]:
#         print(array[-i-1])
#         break
    
# print(array[len(array) - 2])

m = 0
for i in range(len(array)):
    if array[i] > m:
        m = array[i]
        



before = 0
m = 0
for i in range(len(array)):
    if array[i] > m:
        m = array[i]
        before = m
    elif array[i] > before:
        before = array[i]
print(before, m)
