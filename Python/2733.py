class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mina = min(nums)
        maxa = max(nums)

        for i in range(len(nums)):
            if nums[i] != mina and nums[i] != maxa:
                return nums[i]
        return -1
