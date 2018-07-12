"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        myMax = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                myMax = max(myMax, count)
                count = 0
        myMax = max(myMax, count)
        return myMax

"""
Explanation

Have a myMAx counter to track the max consective zeros so far and a count for the current max zeros.
If we see a zero, we increment count. If we see a 1, we take the larger of myMax and count to be the new max and then
set count back to 0.

"""