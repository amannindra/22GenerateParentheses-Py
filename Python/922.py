def sortArrayByParityII(self, nums):
     # check index if divisble by 2
     # even = []
     # odd = []
     # for i in range(len(nums)):
     #     if nums[i] % 2 == 0:
     #         even.append(nums[i])
     #     else:
     #         odd.append(nums[i])
     # e = 0
     # o = 0
     # for i in range(len(nums)):
     #     if i % 2 == 0:
     #         nums[i] = even[e]
     #         e += 1
     #     else:
     #         nums[i] = odd[o]
     #         o += 1
      # return nums
        i = 0
        j = 0
        while j != len(nums):
            even = i % 2 == 0
            odd = j % 2 == 0
            if even and odd:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            i += 2
            j += 2
        return nums
