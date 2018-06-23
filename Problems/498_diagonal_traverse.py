"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000
"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        ROW = 0
        COL = 0

        for row in matrix:
            ROW += 1
            COL = len(row)

        diagonal = []
        for line in range(1, (ROW + COL)):
            # stays in 0 col until we reach bottom of rows
            temp = []
            current_col = max(0, line - ROW)
            count = min(line, ROW, COL - current_col)
            for i in range(0, count):
                temp.append(matrix[min(ROW, line) - i - 1][current_col + i])
            diagonal.append(temp)

        for i in range(0, (ROW + COL) - 1):
            if i % 2 == 1:
                diagonal[i] = diagonal[i][::-1]
                
        output = []
        for row in diagonal:
            for number in row:
                output.append(number)

        return output