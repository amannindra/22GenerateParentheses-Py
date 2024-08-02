class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        dict_1 = {}

        for i in nums:
            start = i[0]
            end = i[1]
            for j in range(start, end + 1):
                dict_1[j] = True

        return len(dict_1.keys())


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        dict_1 = set()

        for i in nums:
            start = i[0]
            end = i[1]
            for j in range(start, end + 1):
                dict_1.add(j)

        return len(dict_1)
