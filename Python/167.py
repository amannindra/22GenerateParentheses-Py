class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if i < j:
        #             if numbers[i] + numbers[j] == target:
        #                 return [i+1, j+1]
        m = len(numbers) - 1
        n = 0
        while m > n: 
            if numbers[m] + numbers[n] > target:
                m -= 1
            elif (numbers[m] + numbers[n] < target):
                n += 1
            else:
                return [n + 1, m + 1]