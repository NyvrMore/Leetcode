"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution(object):
    def reverse(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
            
        start = 0
        end = n - 1
        k = k % n
        
        nums = self.reverse(start, end, nums)
        nums = self.reverse(start, k - 1, nums)
        nums = self.reverse(k, end, nums)

"""
Explanation

Base Cases:
1. We must make sure the shifted amount is within range of the length of the array n

We reverse all the elements in the list, then reverse the first part up to k and reverse the second part after k.

[1,2,3,4,5,6] -> Original
[6,5,4,3,2,1] -> Reverse original
[5,6,4,3,2,1] -> Reverse first part up to k
[5,6,1,2,3,4] -> Reverse second part after k

O(n) time and (1) space

"""