# # SHIT CODE
# class Solution:
#     # def answerQueries(self, nums, queries):
#     #     s = []
#     #     j = []
#     #     c = 0
#     #     nums = sorted(nums)
#     #     i = 0
#     #     while len(s) != len(queries):
#     #         if sum(j) == queries[c]:
#     #             s.append(len(j))
#     #             j = []
#     #             i = 0
#     #             c += 1
#     #         elif sum(j) > queries[c]:
#     #             s.append(len(j) - 1)
#     #             j = []
#     #             i = 0
#     #             c += 1
#     #         elif sum(j) < queries[c] and i == len(queries):
#     #             s.append(len(j) - 1)
#     #             break
#     #         elif nums[i] < queries[c]:
#     #             j.append(nums[i])
#     #             i += 1
#     #         elif nums[i] > queries[c]:
#     #             i = 0
#     #             j = []
#     #         print(f"s: {s}")
#     #         print(f"j: {j}")
#     #         print(f"i: {i}")
#     #         print(f"c: {c}")
#     #         print("================================")
#     #     return s


class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        ans = []
        for val in queries:
            Sum = 0
            counter = 0
            for i in nums: 
                if Sum + i > val:
                    break
                Sum += i
                counter += 1
            ans.append(counter)
        return ans
s = Solution()
s.answerQueries([4,5,2,1], [3,10,21])