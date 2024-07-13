#Works but inefficient
class Solution:
    def sortSentence(self, s: str) -> str:
        word = ""
        l = []
        j = []
        for i in range(len(s)):
            if s[i] == " ":
                l.append(word)
                j.append("")
                word = ""
            else:
                word += s[i]
                print(word)
        
        l.append(word)
        j.append("")
        print(l)        
        for i in range(len(l)):
            g = l[i]
            print(g)
            number = int(g[-1])
            j[number - 1] = g[:-1]
        
        output = ""
        for i in range(len(j)):
            if i == len(j) - 1:
                output += j[i]
            else:
                output += j[i] + " "
            
        return output

class Solution:
    def sortSentence(self, s: str) -> str:
        
        word = ""
        output = ["" for i in range(9)]

        for i in range(len(s)):
            if s[i] == " ":
                idx = int(word[-1])-1
                output[idx] = word
                word = ""
            else:
                word += s[i]

        idx = int(word[-1])-1
        output[idx] = word
        print(output)

        for i in range(len(output)):
            if i == len(j) - 1:
                output += j[i]
            else:
                output += j[i] + " "
            
        return output