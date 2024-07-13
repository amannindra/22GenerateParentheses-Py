class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 1
        nums = sorted(nums)
        s = []

        if len(nums) == 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i]:
                continue
            elif nums[i+1] - nums[i] == 1:
                output += 1
            else:
                s.append(output)
                output = 1
        s.append(output)
        return max(s)
            