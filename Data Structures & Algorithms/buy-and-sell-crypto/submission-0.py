class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        d1 = 0
        d2 = 1
        if len(prices)==1 or len(prices)==0:
            return 0
        temp = prices[d2]-prices[d1]
        for i in range(len(prices)-1):
            if temp<(prices[d2]-prices[d1]):
                temp = prices[d2]-prices[d1]
            if prices[d2]-prices[d1]<0:
                d1=d2
                d2+=1
            else:
                d2+=1
        if temp<=0:
            return 0
        else:
            return temp
            