"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Credits:
Special thanks to @ syedee for adding this problem and creating all test cases.
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
        	return [0]

        if num == 1:
        	return [0,1]

        output = [0,1]
        exp = 1
        cache = {0:0,1:1}
        for i in range(2, num + 1):
        	if i % 2 ** exp == 0:
        		cache[i] = 1
        		exp += 1
        	else:
        		cache[i] = cache[i - 2 ** (exp - 1)] + 1
        	output.append(cache[i])

        return output

"""
Reasoning:

When the nunber is a power of 2, the number of bits is always 1.

Each power of 2 adds another bit. The difference in bits, when the difference between 
two numbers is 2 ** exp, is 1. Therefore, to get the number of 1's in a num, we simply look
in the cache for the number of bits if num - 2 ** exp and add 1.

e.g.

previous info:
21 = 10101 -> 3
cache = {..., 23:3,...}

Get number of 1s:
53 = 110101
since the greatest power of 2 <= 53 is 32, our answer will be
cache[53 - 32] + 1 = cache[21] + 1 = 3 + 1 = 4

"""