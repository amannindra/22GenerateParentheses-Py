class Solution:
    def letterCombinations(self, digits):
        l = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        output = []

        def explore(i, tempStr):
            num = int(digits[i])
            if i < len(digits):
                for j in range(len(l[num-2])):
                    print(j, l[num-2][j])
                    tempStr = l[num-2][j]
                    explore(i+1, tempStr)
            else:
                print(tempStr)
                output.append(tempStr)


        explore(0, '')
        return output


s = Solution()
print(s.letterCombinations("23"))
