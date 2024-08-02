import math


class Solution:
    def accountBalanceAfterPurchase(self, p: int) -> int:
        bank = 100
        s = str(p)
        if int(s[-1]) > 4:
            return bank - int(math.ceil(p / 10.0)) * 10
        else:
            return bank - int(math.floor(p / 10.0)) * 10
