class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_prof = 0
        for price in prices:
            if price < min_price:
                min_price = price
            current_prof = price - min_price
            if current_prof > max_prof:
                max_prof = current_prof
        return max_prof
