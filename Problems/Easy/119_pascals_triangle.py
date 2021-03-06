"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

    1
  1 2 1
 1 3 3 1
1 4 6 4 1

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]
        
        row = [1] * (rowIndex + 1)
        for k in range(2, rowIndex + 1):
            for i in range(k - 1, 0, -1):
                row[i] = row[i] + row[i - 1]
        return row[:rowIndex + 1]

"""
Explanation

We create an array with the size of the index we need. We then constantly update the array until it's the value of the kth index and return it

We can also notice that the value to the right increases by 1 as we incrase the index and the differnce between each following number decreases by 1 until the middle 
then reverses with the gap gettig larger again.
"""