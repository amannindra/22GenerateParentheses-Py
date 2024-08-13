# Trick to find duplicates in an array
# Original:
def findDuplicate(nums: int) -> int:
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]
# better way to find duplicates


def findDuplicate(nums: int) -> int:
    for i in range(0, len(nums)):
            index = nums[i] % len(nums)
            nums[index] += len(nums)

        # nums = 6,8, 9, 7, 7
    for i in range(len(nums)):
        if nums[i] // len(nums) > 1:
            return i