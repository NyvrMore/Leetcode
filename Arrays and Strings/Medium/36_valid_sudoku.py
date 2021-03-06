"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""

class Solution(object):
	def is_unit_valid(self, unit):
		unit = [i for i in unit if i != '.']
		return len(set(unit)) == len(unit)

	def is_row_valid(self, board):
		for row in board:
			if not self.is_unit_valid(row):
				return False
		return True

	def is_square_valid(self, board):
		for i in [0,3,6]:
			for j in [0,3,6]:
				square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
				if not self.is_unit_valid(square):
					return False
		return True

	def is_col_valid(self, board):
		for col in zip(*board):
			if not self.is_unit_valid(col):
				return False
		return True


	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		return self.is_row_valid(board) and self.is_col_valid(board) and self.is_square_valid(board)

"""
Explanation

We use a bunch of helper functions to make this code clean.

is_unit_valid:
	We create an array of all numbebrs in that row that aren't empty. We then compare the length of the array to the set of the array and if they're equal, then all items in the array are unique

is_row_valid:
	we check to see if all all elements in each row are unique, otherwise we return False

is_col_valid:
	we zip the board, which groups all the ith elements of each row together which gives us the columns and then we loop together through them

is_square_valid:
	to validate each square, we consider all squares top left corner (e.g. 00, 03, 06, 30, 33, 36, ect.) We then use list comprehension
	to create an array containing all values in that square by using a double for loop and appending all elements. We then validate if all elements are unique

Using the above functions, if all rows, all columns, and all squares are valid, then we return sudoku
"""

is_row_valid:
	for each row, 
"""