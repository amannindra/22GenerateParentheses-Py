class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if len(s) == 0:
            return True

        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s):
                return True
        return j == len(s)
        