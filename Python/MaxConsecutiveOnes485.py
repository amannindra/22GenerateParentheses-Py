#Teacher
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        c = 0
        m = 0
        for i in nums:
            if i == 1:
                c +=1
            else:
                c = 0
            m = max(m,c)
        return m
        
        
#My version
#Works but not all test cases
#like nums [0]
#expected answer is 0
#but answer returned is 1
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        d = 1
        s = 1
        for i in range(len(nums)-1):
            if(nums[i] == 1):
                d += 1
            else:
                if (d > s):
                    s = d
                d = 1
        if (d > s):
            s = d
        return s

        