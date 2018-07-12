"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution(object):
    def helper(self, n, d):
        if n == 0 or n == 1:
            d[n] = 1
            
        if n not in d:
            d[n] = self.helper(n-1, d) + self.helper(n-2, d)
        
        return d[n]
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return self.helper(n, {})

"""
Explanation

Base Cases:
1. If there are no stairs at at most 1 stairs, the number of distinct ways to climb to the top is 1 
Note: The reason, if n == 0 we are already at the top so there's 1 way

At each state, we can either take 1 step or 2. The sequence turns out to be the fibonacci sequence if we write it out. 
The value at each state of n is the sum of the two prevous computations

"""