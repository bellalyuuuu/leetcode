'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

# Method 1
# Comparing with min: Keep the min_price (min element so far) value along with max_price (max profit so far).
# Find the diff of prices[i] with min_price at each step and update max_price if it exceeds it.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

# Time: O(n)
# Space: O(1)



# Method 2 Kadane's algorithm
# If the current profit becomes negative, start from 0.
# Otherwise add it to current diff p[i] - p[i-1] and update max_profit.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, cur_profit = 0, 0
        for i in range(1, len(prices)):
            cur_profit = max(cur_profit + prices[i] - prices[i-1], 0)
            max_profit = max(cur_profit, max_profit)
        return max_profit

# Time: O(n)
# Space: O(1)



# Method 3
# Brute Force --- Time Limit Exceeded

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j]-prices[i]
                max_profit = max(profit, max_profit)

        return max_profit

# Time: O(n^2)
# Space: O(1)