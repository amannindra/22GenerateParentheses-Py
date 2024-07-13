# more efficient Code
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = 0

        for i in range(len(sentences)):
            s = sentences[i]
            a = 0
            
            for j in range(len(s)):
                if(s[j] == " "):
                    a += 1
            a+=1 
            if a > output:
                output = a
        return output 


        