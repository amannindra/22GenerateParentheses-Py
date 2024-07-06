class Solution:
    def plusOne(self, digits):
        output = ""
        for i in range(len(digits)):
            output += str(digits[i])
        output = int(output)
        output += 1
        output = str(output)
        s = []
        for i in output:
            f = int(i) 
            s.append(f)
        return s
        # s += 1
        # return list(s)