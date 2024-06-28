class Solution:
    def pivotIndex(self, nums) -> int:
        left = 0
        right = 0
        for i in range(len(nums)):
            for j in range(i):
                left += nums[j]
            for k in range(i + 1, len(nums)):
                right += nums[k]
            if(left == right):
                return i
            left = 0
            right = 0
        return -1
    
#O(n^2)

class Solution:
    def pivotIndex(self, nums):
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if(right == left):
                return i
            left += nums[i]
        return -1
#O(2n) faster way