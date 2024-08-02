class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        output = 0
        boxTypes.sort(key=lambda x: -x[1])
        print(boxTypes)
        box = 0
        c = 0
        while box <= truckSize and c < len(boxTypes):
            if truckSize - box > boxTypes[c][0]:
                output += boxTypes[c][0] * boxTypes[c][1]
                box += boxTypes[c][0]
            else:
                output += (truckSize - box) * boxTypes[c][1]
                break
            c += 1

        return output
