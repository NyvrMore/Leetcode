"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]


Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        if matrix == []:
            return matrix
        
        row_length = len(matrix)
        col_length = len(matrix[0])
        rowMatrix = [False] * row_length
        colMatrix = [False] * col_length
        
        for i in range(row_length):
            for j in range(col_length):
                if matrix[i][j] == 0:
                    rowMatrix[i] = True
                    colMatrix[j] = True
        
        print rowMatrix
        print colMatrix
        for i in range(row_length):
            for j in range(col_length):
                if rowMatrix[i] == True or colMatrix[j] == True:
                    matrix[i][j] = 0

"""
Explanation

Base Case
1. If matrix is empty, return matrix

We will use 2 1D arrays to mark which indices of rows and columns are set to 0

We then loop through both rows and columns and if either is true, we set the matrix corresponding to said indicies to 0
"""