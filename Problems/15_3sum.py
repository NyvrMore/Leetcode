"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
        	return []

        nums.sort()
        res = []
        for i, v in enumerate(nums[:-2]): # all possible values of i
        	if i >= 1 and v == nums[i - 1]: # if i is repeated, skip this loop
        		continue
        	d = {}
        	for x in nums[i + 1:]:
        		if x not in d:
        			d[-v-x] = 1
        		else:
        			res += [v, -v-x, x]
        res = list(set(res))
        return res

"""
Explanation

Base Case:
1. The length of nums must be at least 3

We first sort the array. We then enumerate the list for all values of i, this will be our target value while we examine the right side.

We then do a check to see if our current i (target) is different that our previous i, if it's equal we go to the next loop. The reason is that our two sum will find
all unique triples wtith the value of i so we dont need to consider i's of the same value because they will have already been found.

We let x be our iterator on the right side of the loop and we store it like we do in twoSum. Since a + b + c = 0 -> c = - a - b e.g. c = -v - x

As we iterate through the elements in "twoSum", if our element x is not in d, then we add the element that when added to v and x equals 0. e.g. 
v + x + c = 0 -> c = -x-v so for each x not in dictionary, we add -x-v to the dictionary. Then if x is ever in dictionary, it means we've seen both

tl;dr 
i iterates over all values for i
for each i loop, we loop through all x (e.g. nums to the right)
if x isn't in the dictionary, we add its the complement to the dictionary. If x is in the dictionary, that means the pair is matches the target.

x will always greater than -v-x since when we add the array, it's when the pair has been completed. giving us [v, -v-x, x]
"""