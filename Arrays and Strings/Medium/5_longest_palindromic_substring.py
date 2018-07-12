"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)

        if n == 0:
            return 0

        max_len = 1
        palindromeStartingIndex = 0
        LP = [[None for i in range(n)] for j in range(n)]
        
        # length 1
        for i in range(n):
            LP[i][i] = True
            
        # length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                max_len = 2
                palindromeStartingIndex = i
                LP[i][i+1] = True
                
        # length > 2
        for curr_len in range(3, n+1):
            for i in range(n - curr_len + 1):
                j = i + curr_len - 1
                if s[i] == s[j] and LP[i+1][j-1]:
                    max_len = curr_len
                    palindromeStartingIndex = i
                    LP[i][j] = True
        return s[palindromeStartingIndex:palindromeStartingIndex + max_len]

"""
Explanation

Base Case:
1. If n == 0, we return 0

We use a 2D matrix to track the palindrome. The max length palindrome of any single character is 1 so we initialize our max_len to 1. Our initial palindrome starting index is 0

The diagonal represents individual characters so they're all initialized to 1.

We then use a for loop to handle all characters of length 2 since the element to the bottom left is None. If the characters are equal, we increment the palindrome length to 2 and 
let the starting index be i (which will be the index of the first character of the string) and let the right most character of the palindrome be true (the others have already been filled in)

For all strings of length 3 or greater, (the bottom left has been filled in so we can use it) we then loop through all palindromes of that length and if found, we update the matrix

We return the indicies of the string where the left index is the starting index of the palindrome and the right index is the starting index + max_len

[True, None, True, None, None]
[None, True, None, True, None]
[None, None, True, None, None]
[None, None, None, True, None]
[None, None, None, None, True]

"""