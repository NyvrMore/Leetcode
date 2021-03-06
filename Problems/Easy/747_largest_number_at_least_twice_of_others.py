"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        myMax = nums[0]
        myIndex = 0
        for i in range(1, len(nums)):
            if nums[i] > myMax:
                myMax = nums[i]
                myIndex = i

        double = True
        for i in range(len(nums)):
            if myMax < nums[i] * 2 and i != myIndex:
                double = False

        if double:
            return myIndex
        return -1

"""
Explanation

We find the maximum value in the array and the index of that number. We then loop through each element and
check to see if max is at least twice as big as every other element except for the element itself
"""