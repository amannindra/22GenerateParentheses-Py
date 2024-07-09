#This is the SHITTEST code I have ever written in my life.
# This is 0(n) complexity
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x + 1):
            if i*i > x:
                return i - 1
            elif i*i == x:
                return i
        return 0
    
print(14//5)
    
            
#This is better solution, but I watched a video

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right:
            mid = math.ceil(left + (right - left)/2)
            if mid*mid <= x:
                left = mid
            else:
                right = mid-1
        return left
    
#I'm so dumb. This was so easy.            
            