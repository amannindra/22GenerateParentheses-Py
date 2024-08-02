class Solution:
    def isGood(self, nums: List[int]) -> bool:

        nums = sorted(nums)
        m = max(nums)
        output = 0
        if (len(nums) != m + 1):
            return False

        mydict = {}
        for i in range(len(nums)):
            if nums[i] not in mydict:
                mydict[nums[i]] = 1
            else:
                mydict[nums[i]] += 1
        if mydict[m] != 2:
            return False

        print(mydict)
        return True
