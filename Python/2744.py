class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ignore = []
        output = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][::-1] and words[i] not in ignore and words[j][::-1] not in ignore:
                    output += 1
                    ignore.append(words[i])
                    ignore.append(words[j])
        return output