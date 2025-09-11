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

        # Use a list to store mutable values for start and max_len
        state = [0, 1] # [start, max_len]

        # Helper function to expand around a center
        def expand_around_center(left, right):
            # Access and modify the list elements
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > state[1]: # state[1] is max_len
                    state[1] = current_len
                    state[0] = left      # state[0] is start
                left -= 1
                right += 1

        for i in range(n):
            # For odd length palindromes (e.g., "aba")
            expand_around_center(i, i)
            # For even length palindromes (e.g., "abba")
            expand_around_center(i, i + 1)

        return s[state[0]:state[0] + state[1]]
```