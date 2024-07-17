class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        output = 1
        current = 1
        for i in range(len(s)-1):
            if (ord(s[i]) + 1 == ord(s[i+1])):
                current += 1
                print(current)
                if current > output:
                    output = current
            else:
                current = 1
        return output