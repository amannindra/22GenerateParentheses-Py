class Solution:
    def findContentChildren(self, g, s) -> int:
        g = sorted(g)
        s = sorted(s)
        y = 0
       

        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if g[y] <= s[i]:
                print(g, s[i])
                y +=1
            if y == len(g):
                return y
        return y