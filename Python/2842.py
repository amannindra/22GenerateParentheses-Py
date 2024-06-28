class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        output = 0
        for i in range(low, high+1):
            if(len(str(i)) % 2 ==0):
                s = str(i)
                s = list(s)
                out = 0
                oin = 0
                for g in range(len(s)):
                    s[g] = int(s[g])
                for k in range(len(s)):
                    if(k < len(s)/2):
                        out += s[k]
                    else:
                        oin += s[k]
                if (out == oin):
                    output += 1
        return output
                        