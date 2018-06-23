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
        
        isPos = True # flag as negative and make positive
        if x < 0:
            x = 0 - x
            isPos = False
            
        reverse = 0     # get the reverse form
        while x is not 0:
            reverse = reverse * 10 + x % 10
            x /= 10
            
        if not isPos: # if it was negative, make it negative again
            reverse = 0 - reverse
            
        if reverse.bit_length() > 31: # check to see if it's 32 bit; 1 bit used to check sign 
            return 0
        return reverse