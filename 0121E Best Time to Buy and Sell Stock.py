'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        profit = 0
        while r < n :
            if prices[l] < prices[r]:                           # check if we have min buying price than current buying price
                profit = max(profit, prices[r] - prices[l])     # update the current profit
            else:                                               # when we find min buying price than current one   
                l = r                                           # because r is the new minimum buying price
            r += 1                                              # increment r
        return profit                                           # return the profit

mySol = Solution()
prices = [2,1,2,1,0,1,2]
print(mySol.maxProfit(prices))