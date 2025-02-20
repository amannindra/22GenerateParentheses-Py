class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        m5 = 0
        m10 = 0
        m20 = 0
        for i in range(len(bills)):
            if(bills[i] == 5):
                m5 += 1
            elif(bills[i] == 10):
                m5 -= 1
                m10 += 1
            else:
                # m5 -= 1
                # m10 -= 1
                # m20 += 1
                if(m10 > 0 and m5 > 0):
                    m10 -= 1
                    m5 -= 1
                else:
                    m5 -= 3
                    m20 += 1
            if(m5 < 0 or m10 < 0):
                return False
        

        return True
        