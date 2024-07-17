class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict = {}
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = 1
            else:
                my_dict[s[i]] += 1
        print(my_dict)

        l = []
        for i in my_dict:
            l.append([i,my_dict[i]])
        print(l)
        l.sort(key=lambda x:-x[1])
        print(l)
        output = ""
        for i in range(len(l)):
            for j in range(l[i][1]):
                output += l[i][0]
        return output