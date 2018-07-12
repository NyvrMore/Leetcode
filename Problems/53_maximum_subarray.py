"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)

		if n == 0:
			return 0

		global_max = -float('inf')
		current_max = -float('inf')
		for i in range(n):
			current_max = max(current_max + nums[i], nums[i])
			if global_max < current_max:
				global_max = current_max
			
		return global_max

"""
Explanation

Base Cases:
1. if nums is empty, we return 0

We track the current max and a global max. 

If nums isn't empty, then our global max is updated to the first item and it's our current max.

We then iterate through nums. At each item, we update current max to the larger of our current max and current max + current element
We then check to see if our current max is greater than our global max, if it is then we update global max

we return global max
"""


