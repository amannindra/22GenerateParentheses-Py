class Solution:
    def restoreString(self, s: str, indices) -> str:
        output = []
        for i in range(len(s)):
            output.append("")
        for i in range(len(s)):
            output[indices[i]] = s[i]

        return "".join(output)