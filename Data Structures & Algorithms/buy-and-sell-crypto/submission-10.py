class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        minB=prices[0]
        for sell in prices:
            profit=sell-minB
            maxP=max(maxP,profit)
            minB=min(minB,sell)
        return maxP                  

                 
                
                
