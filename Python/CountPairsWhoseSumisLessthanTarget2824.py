class Solution:
    def countPairs(self, nums, target) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i < j):
                    if(nums[i] + nums[j] < target):
                        output += 1
            
        return output
        