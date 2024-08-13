def removeAnagrams(self, words: List[str]) -> List[str]:
     # b
     # for i in range(len(words)):https://leetcode.com/problems/count-number-of-teams/
     #     words[i] = sorted(words[i])
     # print(words)
    i = 0
    a = []
    while i < len(words):
        j = i
        print(f"{words[i]} === {words[j]}")
        while j < len(words) and sorted(words[i]) == sorted(words[j]):
            j += 1
        a.append(words[i])
        i = j
    return a
