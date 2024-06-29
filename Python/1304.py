class Solution:
    def sumZero(self, n: int) -> int:
        output = []
        if n == 1:
            output.append(0)
            return output
        else:
            for i in range(1, n//2 + 1):
                output.append(i)
                output.append(-i)
                print(output)

        if n > len(output):
            output.append(0)
            return output
        return output