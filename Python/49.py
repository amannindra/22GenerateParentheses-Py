class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output = []
        # j = 0
        # test = []
        # for i in range(len(strs)):
        #     strs_sorted = sorted(strs[i])
        #     test.append("".join(strs_sorted))
        # print(test)
        # vis = set()
        # for i in range(len(test)):
        #     l = []
        #     for j in range(i, len(test)):
        #         if j in vis:
        #             continue
        #         if test[i] == test[j]:
        #             l.append(strs[j])
        #             vis.add(j)
        #     if l:
        #         output.append(l)
        # print(output)
        # return output
        d = {}
        for i in strs:
            SortedString = "".join(sorted(i))
            if SortedString not in d:
                d[SortedString] = [i]
            else:
                d[SortedString].append(i)
        output = []
        for val in d.values():
            output.append(val)
        return output
    