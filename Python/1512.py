class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        mydict = {}
        for i in range(len(nums)):
            if(nums[i] in mydict):
                mydict[nums[i]] += 1
            else:
                mydict[nums[i]] = 1

        for i in mydict.values():
            output += int((i*(i-1))/2)
        return output


