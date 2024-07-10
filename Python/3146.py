class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        output = 0
        my_dicts = {}
    
        for i in range(len(s)):
            my_dicts[s[i]] = i
        for i in range(len(t)):
            output += abs(i - my_dicts[t[i]])
        

        return output