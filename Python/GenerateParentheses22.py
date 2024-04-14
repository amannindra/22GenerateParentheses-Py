class Solution:
    def generateParenthesis(self, n):
        l = []
        def gen(temp, n, left, right, step):
            if(left == n and right == n):
                l.append(temp)
                return
            if(left < n):
                gen(temp +"(", n, left+1,right, step +1)
            if(right<left):
                gen(temp + ")", n, left, right+1, step+ 1)
            return

        temp = ""
        gen(temp,n,0,0,0)
        return l
s = Solution()
print(s.generateParenthesis(2))