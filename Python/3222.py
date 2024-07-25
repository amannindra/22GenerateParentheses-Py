class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        output = "Bob"
        while x > 0 and y > 3:
            if output == "Bob":
                output = "Alice"
            else:
                output = "Bob"
            print(output)
            x -= 1
            y -= 4
        return output
    
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        
        s = min(x, y//4) 
        
        # if y > 4*x:
        #     y = y // 4

        if s % 2 == 1:
            return "Alice"
        else: 
            return "Bob"


        # output = "Bob"
        # while x > 0 and y > 3:
        #     if output == "Bob":
        #         output = "Alice"
        #     else:
        #         output = "Bob"
        #     print(output)
        #     x -= 1
        #     y -= 4
        # return output