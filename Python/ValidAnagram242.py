#Teacher help me fix sintax errors
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def st(strt):
            my_dicts = {}
            for i in range(len(strt)):
                if strt[i] not in my_dicts:
                    my_dicts[strt[i]] = 1
                else:
                    my_dicts[strt[i]] += 1
            return(my_dicts)

        return st(s) == st(t)