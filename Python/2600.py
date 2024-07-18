class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        output = 0
        
        if k > numOnes:
            output += numOnes
            k  -= numOnes
        else:
            output += k
            return output
        if k > numZeros:
            k -= numZeros
        else:
            return output
        if k > numNegOnes:
            k -= numNegOnes
            output -= numNegOnes
        else:
            output -= k
            return output
        return output


        # for i in range(k):
        #     if numOnes > 0:
        #         output += 1
        #         numOnes -= 1
        #     elif numZeros > 0:
        #         numZeros -= 1
        #     elif numNegOnes:
        #         output -= 1
        #         numNegOnes -= 1
        # return output


            