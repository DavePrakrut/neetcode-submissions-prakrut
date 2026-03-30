class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxP=0
        MinB=prices[0]
        for sell in prices:
            MaxP=max(MaxP,sell-MinB)
            MinB=min(MinB,sell)
        return MaxP    
                 

        