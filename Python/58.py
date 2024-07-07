#LAZY ASS WAY
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        return len(x[-1])
            
#not the most efficient Way, but it works
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        output = ""
        i = len(s) - 1
        if len(s) < 3:
            return 1
        while i >= 0:
            if(s[i] == " "):
                if(len(output) > 0):
                    return len(output)
            else:
                output += s[i]
            i -= 1
        return len(output)