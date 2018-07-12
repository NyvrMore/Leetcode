"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        upper = len(matrix) - 1
        lower = 0
        
        while lower < upper:
            for i in range(upper-lower):
                matrix[lower][lower + i], matrix[lower + i][upper], matrix[upper][upper - i], matrix[upper - i][lower]  = matrix[upper - i][lower], matrix[lower][lower + i], matrix[lower + i][upper], matrix[upper][upper - i]
            lower += 1
            upper -= 1
"""
Explanation

let lower be the left most index and upper be the right most. At each level, we do upper-lower loops and swap all corners, then their neighers ect.
After we do n swaps, we increment lower and decrement upper and repeat this for each level
"""