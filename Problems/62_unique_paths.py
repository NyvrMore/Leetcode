"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there? 

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        DP = [[None for col in range(n)] for row in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    DP[i][j] = 1
                else:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]
                    
        return DP[m-1][n-1]

""" 
Explanation

Base Cases:
1. If  m or n is 0, then DP[i][j] = 0 since we're either going straight left or straight down which there is only 1 path

Logic:
At each i,j where i,j > 0, the number of unique paths at any index is the sum of both converging paths (i.e. the path from above and from the left). 

We return the bottom right of the matrix
"""
