#Works and I did by myself
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        start = 0
        direction = True
        for i in range(time + 1):
            if(direction):
                start += 1
            else:
                start -= 1
            if(start == n or start == 1):
                if(i != 0):
                    direction = not direction

            print(start)