"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        padding = max(len(a),len(b)) - min(len(a),len(b))

        if len(a) > len(b):
            b = "0" * padding + b
        elif len(a) < len(b):
            a = "0" * padding + a

        output = ""
        carry = False
        for i in range(len(a) - 1, -1, -1):
            if a[i] == "0" and b[i] == "0" and not carry:
                output = "0" + output
            elif ((a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0")) and not carry:
                output = "1" + output
            elif a[i] == "1" and b[i] == "1" and not carry:
                output = "0" + output
                carry = True
            elif a[i] == "0" and b[i] == "0" and carry:
                output = "1" + output
                carry = False
            elif ((a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0")) and carry:
                output = "0" + output
                carry = True
            elif a[i] == "1" and b[i] == "1" and carry:
                output = "1" + output
        if carry:
            output = "1" + output

        return output

"""
Explanation

We find the difference between the length of a and b and add padding so they're equal length. 
We then loop starting from right most and moving left and adding the values and keep tracking if there's
a carry or not.
"""