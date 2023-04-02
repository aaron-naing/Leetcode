"""
Problem Statement:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1

        quo = abs(x)
        rev = 0
        while quo:
            quo, remain = divmod(quo, 10)
            rev = rev * 10 + remain
        return sign * rev if -2**32 <= rev <= 2**31 -1 else 0 
