def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return nums

    s = []
    a = []
    for i in range(len(nums)):
        if nums[i] != 0:
            s.append(nums[i])
        else:
            a.append(nums[i])
    print(s, a)
    array = s + a
    for i in range(len(nums)):
        print(i)
        nums[i] = array[i]
    return nums
# Better way


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return nums

    i = 0
    j = 0
    n = len(nums)
    while i < n and j < n:
        if nums[j] == 0:
            j += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            i += 1
