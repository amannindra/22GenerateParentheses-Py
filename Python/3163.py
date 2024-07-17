# "aaabbaaccccd"
# 3a2b2a4c1d

class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        l1 = []
        num = 1
        i = 0

        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                num += 1
                if num == 9:
                    l1.append(str(num))
                    l1.append(word[i])
                    num = 1
            else:
                l1.append(str(num))
                l1.append(word[i])
                num = 1
            i += 1

        l1.append(str(num))
        l1.append(word[i])

        return "".join(l1)


d = Solution()

print(d.compressedString("aaabbaaccccd"))
