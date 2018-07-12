# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 and isBadVersion(1):
            return n
   
        left, right = 1, n
        while left < right:
            mid = (left + right) / 2
            if isBadVersion(mid) == False and isBadVersion(mid + 1) == True:
                return mid + 1
            elif isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid
                
        if left != n and isBadVersion(left) == False:
            return left + 1
        else:
            return left

"""
Explanation

We do an advanced binary search - which allows us to access the right neighbor

If the the next is true while the current is false, then the next is the is the bad version
so we return the index of it

else if the current is false, we increment left to search the right half

otherwise it was true so we search the left half

We finally do the end check to check if that left is not the final index and that if it's false,
the bad index must be the last node, OW it's the current
"""
