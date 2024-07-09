#Dosen't work

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1] and nums[i] != "_":
                nums.remove(nums[i])
                nums.append("_")
                i -= 1
            i += 1
            print("problem here: " + str(i))

        c = 0
        while nums[c] != "_":
            c += 1
        return c, nums


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


#Ended up copying the code: 
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        c = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[c] = nums[i]
                c+= 1
        return c




