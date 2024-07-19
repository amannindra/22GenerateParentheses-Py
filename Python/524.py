class Solution:
    def findLongestWord(self, s, dictionary) -> str:
        output = ""
      
        if len(s) == 0:
            return ""
        y = 0
        for i in range(len(dictionary)):
            for j in range(len(s)):
                print(dictionary[i], y)
                if dictionary[i][y] == s[j]:
                    # print(dictionary[i][y],y, len(dictionary[i]))
    
                    y += 1
                    if y == len(dictionary[i]):
                        if y > len(output):
                            output = dictionary[i]
                        if y == len(output) and dictionary[i] < output:
                            output = dictionary[i]
                        break
            y = 0
        return output
            
               
                
s = Solution()
print(s.findLongestWord("abpcplea", ["ale","apple","monkey","plea", "abpcp"]))

print('--------------------------------------------------------')
print(s.findLongestWord("abpcplea",["a","b","c"]))
