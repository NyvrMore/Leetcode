"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        output = []
        for line in range(1, numRows + 1):
            temp = []
            if line < 3:
                for i in range(line - 1):
                    temp.append(1)
            else:
                for i in range(line - 1):
                    if len(temp) == 0:
                        temp.append(1)
                    else:
                        temp.append(sum(output[line - 2][i - 1: i + 1]))
            temp.append(1)
            output.append(temp)
        return output

"""
Explanation

We handle the base case where n < 3. If n = 0, we return the empty list, if n = 1, we append 1, and for n = 2 we append two 1's.
For n > 2, the value for index 0 will always be 1. Then the follow index is the sum of the number at the same index in the prev list
and it's right neighbor. After we're done looping, we append a 1 at the end for each layer.
"""