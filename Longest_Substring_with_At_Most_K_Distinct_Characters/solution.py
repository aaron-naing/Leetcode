
"""
Problem Statement:
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashmap = {}
        maxLen = 0
        front = 0
        back = 0
        if k == 0:
            return 0
        while front < len(s):
            if s[front] in hashmap:
                hashmap[s[front]] = front
            else:
                if len(hashmap) < k:
                    hashmap[s[front]] = front
                else:
                    # find the key with lowest value
                    to_replace = min(hashmap, key=hashmap.get)
                    back = hashmap[to_replace] + 1
                    del hashmap[to_replace]
                    hashmap[s[front]] = front
            maxLen = max(maxLen, front - back + 1)
            front += 1
        return maxLen