class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)):
            if(i < len(s)-1 and my_dict[s[i]] < my_dict[s[i+1]]):
                num -= my_dict[s[i]]
            else: 
                num += my_dict[s[i]]

        return num   