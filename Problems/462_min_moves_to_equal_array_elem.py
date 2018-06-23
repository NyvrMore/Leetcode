"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def merge(S1, S2, S):
            """ Merge two sorted python lists S1 and S2 into properly sized list S """
            i = j = 0
            while i + j < len(S):
                        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):		
                            S[i+j] = S1[i]										
                            i += 1
                        else:
                            S[i+j] = S2[j]										
                            j += 1

        def mergesort(S):
            """ Sort the elements of S """
            n = len(S)
            if n < 2:			
                return
            mid = n / 2
            S1 = S[:mid]
            S2 = S[mid:]

            mergesort(S1)		
            mergesort(S2)		

            merge(S1, S2, S)
            
        if len(nums) < 2:
            return 0
        mergesort(nums)
        mid = len(nums) / 2
        result = 0
        for num in nums:
            result += abs(num - nums[mid])
        return result