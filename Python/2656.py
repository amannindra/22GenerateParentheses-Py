class Solution:
    def maximizeSum(self, nums, k: int) -> int:
        s = max(nums) #O(n)
        output = 0
        for i in range(k): #O(k)
            output += s
            s += 1
        return output

        #O(nlogn) + O(k)        
