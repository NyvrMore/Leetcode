"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
s
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        ROW = 0
        COL = 0

        for row in matrix:
            ROW += 1
            COL = len(row)


        ROW = 0
        COL = 0

        for row in matrix:
            ROW += 1
            COL = len(row)


        last_row = ROW 
        last_col = COL 
        k = 0
        l = 0

        output = []
        while(k < last_row and l < last_col):
            
            for i in range(l, last_col):
                output.append(matrix[k][i])
            k += 1

            for i in range(k, last_row):
                output.append(matrix[i][last_col - 1])
            last_col -= 1

            if (k < last_row):
                for i in range(last_col - 1, l  -  1, -1):
                    output.append(matrix[last_row - 1][i])
                last_row -= 1

            if (l < last_col):
                for i in range(last_row - 1, k - 1, -1):
                    output.append(matrix[i][l])
                l += 1

        return output