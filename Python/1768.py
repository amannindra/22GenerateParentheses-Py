class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            output += word1[i]
            output += word2[i]
            i += 1
            j += 1
        if i < len(word1):
            output += word1[i:]
        if j < len(word2):
            output += word2[j:]
        return output
            
        #0(max(n,m))