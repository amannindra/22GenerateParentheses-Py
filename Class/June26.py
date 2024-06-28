class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = min(nums)
        min_index = -1
        for i in range(len(nums)):
            if nums[i] == n:
                min_index = i
        cur = min_index
        for s in range(len(nums) -1):
            cur = cur % len(nums)
            nex = (cur + 1) % len(nums)
            if nums[cur] <nums[nex]:
                cur +=1
                continue
            else:
                return -1
        if(len(nums) == len(nums) - min_index):
            return 0
        return len(nums) - min_index




        # return len(nums) - num.index(num(nums)) if 
        # num = sorted(nums)
        # rotation = 0
        # for i in range(len(nums)):
        #     if(num != nums):
        #         nums.insert(0, nums.pop())
        #         rotation += 1
        #     else:
        #         return rotation
        # return -1