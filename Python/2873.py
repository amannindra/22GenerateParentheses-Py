import time

class Solution:
    def version1(nums):
        output = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i < j < k:
                        if (nums[i] - nums[j]) * nums[k] > output:
                            output = (nums[i] - nums[j]) * nums[k]
        return output

    def version2(nums):
        output = 0
        l = []
        m = -1
        for i in nums:
            m = max(i, m)
            l.append(m)
        print(l)

        p = 0
        for j in range(1, len(nums)):
            for k in range(j + 1, len(nums)):
                a = l[j - 1]
                b = nums[j]
                c = nums[k]
                p = max((a-b)*c, p)
        return p

    def version3(nums):
        start = time.time()
        s = 100
        i = 1
        while i <= s:
            if s % i == 0:
                i += 1
            print(i)
            i += 1
        end = time.time()
        print(f"Iteration: {i}\tTime taken: {(end-start)*10**3:.03f}ms")


Solutio = Solution()
Solutio.version3()
