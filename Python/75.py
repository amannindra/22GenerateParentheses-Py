class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(0, len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
            print(nums)
        return nums
