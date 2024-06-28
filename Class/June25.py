

num = [4, 5, 1, 2, 3]

if (num == sorted(num)):
    print("true")


n = 0
for i in range(len(num)-1):
    if (num[i] < num[i+1]):
        continue
    else:
        print("stop")
        break

a = [4, 5, 1, 2, 3]


c = 0
for i in range(len(a)):
    if (a != sorted(a)):
        a.insert(0, a[-1])
        a.pop()
        c += 1

print(c)

len(a) - a.index(min(a))

arr = [1, 2, 3, 4, 5]
for i in range(len(arr)//2 + 1):
    temp = arr[i]
    arr[i] = arr[-i - 1]
    arr[-i - 1] = temp
    print(f"step: {i}: {a}")
print(arr)

strs = "naasde"
stra = "naaassde"

# f = True
# for i in range(len(strs)):
#     if strs[i] in stra:
#         strs[i] = ""
#     else:
#         f = False
#         break
# if (f):
#     print("its an anagram")
# else:
#     print('no')

v = "supermans"
v = sorted("supermans")
print(v)
g = "perssunam"
g = sorted("perssunam")
print(g)

print('------')
arrs = [1, 1, 3, 1, 1, 2, 5, 2, 2, 3]
arrs = sorted(arrs)
my_dict = {}
for i in range(len(arrs)):
    if arrs[i] not in my_dict:
        my_dict[arrs[i]] = 1
    else:
        my_dict[arrs[i]] += 1
print(my_dict)
print("--------------------------")

v = "supermans"
my_dicts = {}

for i in range(len(v)):
    if v[i] not in my_dict:
        my_dicts[v[i]] = 1
    else:
        my_dicts[v[i]] += 1
print(my_dicts)
print('---------------')
h = "perssunam"
my_dictsg = {}

for i in range(len(h)):
    if v[i] not in my_dict:
        my_dictsg[v[i]] = 1
    else:
        my_dictsg[v[i]] += 1
print(my_dictsg)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        d = 1
        s = 1
        for i in range(len(nums)-1):
            if(nums[i] == 1):
                d += 1
                if (d > s):
                    s = d
                d = 1
        if (d > s):
            s = d
        return s
    
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        m = 0
        for i in nums:
            if i == 1:
                c +=1
            else:
                c = 0
            m = max(m,c)
        return m



