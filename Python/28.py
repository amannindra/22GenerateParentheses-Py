class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            output = 0
            j = 0
            if haystack == needle:
                return 0
            for i in range(len(haystack)):
                if j == len(needle):
                    print('sdfs')
                    return output
                if haystack[i] == needle[j]:
                    if j == 0:
                        output = i
                    print('hdfg')
                    j += 1
                else:
                    print('nkj')
                    j = 0

        return -1


s = Solution()
print(s.strStr("a", "a"))
