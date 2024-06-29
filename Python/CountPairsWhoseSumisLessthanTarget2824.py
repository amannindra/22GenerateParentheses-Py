class Solution:
    def countPairs(self, nums, target) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i < j):
                    if(nums[i] + nums[j] < target):
                        output += 1
            
        return output
    


#ALOT BETTER
    def countPair(self, nums, target: int) -> int:
        output = 0
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < target:
                output += j - i
                i += 1
            else:
                j -= 1
        return output
        
S = Solution()
S.countPairs([-6,2,5,-2,-7,-1,3],-2)