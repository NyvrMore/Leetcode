"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

class Solution(object):
	def helper(self, nums, n, d):
		if n == 1:
			d[n] = nums[n-1]

		if n == 2:
			d[n] = max(nums[n - 1], nums[n-2])

		if n not in d:
			if n-1 not in d:
				d[n] = max(self.helper(nums, n-1, d), nums[n - 1] + self.helper(nums, n - 2, d))
			else:
				d[n] = max(d[n-1], nums[n - 1] + self.helper(nums, n - 2, d))

		return d[n]

	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if nums == []:
			return 0

		return self.helper(nums, len(nums), {})

	"""
	Notes:
	Since we can't rob adjacent houses, we must choose the house that'll ultimately
	give us the greatest profit. Therefore, the max profit at after each house n is the max between
	the current house and the one previous
	"""