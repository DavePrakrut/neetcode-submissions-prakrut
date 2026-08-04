class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minb=prices[0]
        maxp=0
        for sell in prices:
            maxp=max(maxp,sell-minb)
            minb=min(minb,sell)
        return maxp    