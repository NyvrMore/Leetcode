"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        s = 0
        for digit in digits:
            s = digit + s * 10

        s += 1
        output = []
        while s > 0:
            output = [s % 10] + output
            s /= 10

        return output

"""
Explanation

s will be the sum for our output. We build sum by looping thorugh digits. We then increment s by 1 then add its
digits into a list. Note, we want the result of the mod on the left. Then return output
"""

