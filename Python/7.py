#This is dumbest way to reverse an Int. Look at this shit code 
class Solution:
    def reverse(self, x: int) -> int:
        g = list(str(x))
        if x < 0:
            g.pop(0) 
        b = 0
        r = len(g) - 1
        while b < r:
            temp = g[b]
            g[b] = g[r]
            g[r] = temp
            b += 1
            r -= 1
        num = 0
        for digits in g:
            num = num * 10 + int(digits)
        if num > -pow(2,31) and num < pow(2,31) - 1:
            return -num if x < 0 else num
        else:
            return 0

#This is good code
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        
        if rev > 2**31 - 1 or rev < -2**31:
            return 0
        
        return rev