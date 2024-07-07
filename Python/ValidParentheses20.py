
#Version one
# This is one of shitttttest codes I have ever written
# wtf am I doing
# also it dosen't work
class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        while i < len(s) - 1:
            print(i)
            print(f"This is {s[i]} and {s[i+1]}")
            if(s[i] == '(' and s[i+1] == ")"):
                i += 2
                continue
            elif(s[i] == '[' and s[i+1] == "]"):
                i += 2
                continue
            elif(s[i] == '{' and s[i+1] == "}"):
                i += 2
                continue
            else:
                return False
        return True
    

#Good Code but not fully correct
#Looked a answer for a few seconds 
#Then created my own version of the answer
#dosen't work for "([)]"
#Expected is False but my answer is True

class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for c in s:
            print(f"a:{a}")
            print(f"c: {c}")
            if c in "([{":
                a.append(c)
            else:
                if c == ")" and "(" in a:
                    a.remove("(")
                    continue
                elif c == "}" and "{" in a:
                    a.remove("{")
                    continue
                elif c == "]" and "[" in a:
                    a.remove("[")
                    continue
                else:
                    return False
        return True
    
# Sol = Solution()
# print(Sol.isValid("([)]"))

stack = ["asd",'adsda', 'ads']
print(stack.pop())
stack = stack.pop()
print(stack)
    
    
#Version 3
#Work on this problem for the past hour. Ended up watching a video.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if (len(s) % 2 == 0):    
            mapping = {")": "(", "}": "{", "]": "["}
            for i in s:
                if i in mapping.values():
                    stack.append(i)
                else:
                    if not stack or mapping[i] != stack.pop():
                        return False
            return not stack
        else:
            return False
        