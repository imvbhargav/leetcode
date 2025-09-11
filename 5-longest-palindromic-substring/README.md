# 5. Longest Palindromic Substring

## Problem

Given a string s, return the longest palindromic substring in s.

 
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


Example 2:

Input: s = "cbbd"
Output: "bb"


 
Constraints:


	1 <= s.length <= 1000
	s consist of only digits and English letters.

## Solution

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s
        max = ""
        for i in range(len(s)):
            for j in range(n, i, -1):
                subs = s[i:j]
                if subs == subs[::-1] and len(subs) > len(max):
                    max = subs
        return max
                    
```