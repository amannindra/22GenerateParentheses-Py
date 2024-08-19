# works but effency sucks

def findTheLongestBalancedSubstring(self, s: str) -> int:
    output = []
    for i in range(len(s)):
        word = ""
        for j in range(i, len(s)):
            word += s[j]
            output.append(word)
    print(output)
    ret = 0
    for i in range(len(output)):
        s = output[i]
        j = 0
        zero = 0
        ones = 0
        while j < len(s) and s[j] == "0":
            zero += 1
            j += 1
        while j < len(s) and s[j] == "1":
            ones += 1
            j += 1
        print(zero, ones, s)
        if ones > ret and zero >= ones and zero + ones == len(s):
            ret = ones
            print(f"ret: {ret}")

    return ret * 2
