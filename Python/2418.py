class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h = list(zip(heights, names))
    
        # d = sorted(h, reverse = True)
        
        # l = []
        # for i in range(len(names)):
        #     l.append(d[i][1])
        # return l
        h.sort(key=lambda x:-x[1])
        l = []
        for i in range(len(names)):
            l.append(h[i][1])
        return l
