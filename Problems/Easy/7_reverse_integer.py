"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        neg = False
        if x < 0:
            neg = True
            x = -1 * x
        
        s = 0
        while x > 0:
            s = x % 10 + s * 10
            x /= 10
            
        if neg:
            s = -1 * s
        if (-1 * (1 << 31)) < s < ((1 << 31) - 1): # check 32 bit range [-2^31, 2^31 - 1] note, 0 included in positive half
            return s
        else:
            return 0

""" 
Explanation

We first check if number is negative and track it. Then we reverse the integer and make it negative again if it was previously.
Lastly, we check the range.

"""