"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        DP = [0] + [float('inf')] * amount
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    DP[i] = min(DP[i], DP[i-coin] + 1)
                    
        if DP[-1] == float('inf'):
            return -1
        return DP[-1]

"""
Explanation

We initialize an array of length n + 1 to handle all values between 0 and n inclusively. For i = 0, DP[i] = 0 since
the it takes 0 coins to make 0. The rest are initialized to infinity until we find them.

For each amount, we determine the maximum number of coins it takes to make that amount. We do this by looping through the
coins and checking to see if the index i - coin >= 0. What this means is that number of coins to make the amount i is equal to the number of 
coins used to make the amount at DP[i - coin] + 1. We do this for each coin and take the minimum number of coins possible.

We return the last index of the array or -1 if it's infinity
"""