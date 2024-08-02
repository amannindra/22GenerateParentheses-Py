#NAWW, this is definitely the shittest code I have ever written
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        output = -1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                maxnum1 = 0
                for digit in str(nums[i]):
                    digit = int(digit)
                    if digit > maxnum1:
                        maxnum1 = digit
                maxnum2 = 0
                for digits in str(nums[j]):
                    digits = int(digits)
                    if digits > maxnum2:
                        maxnum2 = digits
                if maxnum1 == maxnum2 and nums[i] + nums[j] > output:
                    output = nums[i] + nums[j]
        return output
