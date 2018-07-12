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
Explaination

Base Case:
1. If n is empty, the number of ways is 1
2. If n is 1, th enumber of ways is 1

The number of ways to climb distinct steps if the sum of both the previous (1 steps taken), and 2 steps (2 step taken). We use a helper function since we need to 
handle maintain a dictionary and pass it through and return it

"""