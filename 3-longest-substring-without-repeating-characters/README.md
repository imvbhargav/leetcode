# 3. Longest Substring Without Repeating Characters

## Problem

Given a string s, find the length of the longest substring without duplicate characters.

 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


 
Constraints:


	0 <= s.length <= 5 * 104
	s consists of English letters, digits, symbols and spaces.

## Solution

```Python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}  # Stores the last seen index of each 
character
        max_length = 0
        start = 0  # Start of the sliding window

        for end in range(len(s)):
            current_char = s[end]

            # If the current character is already in the map and 
its last seen index
            # is within the current window (i.e., greater than or 
equal to 'start'),
            # it means we have a repeating character. We need to 
move the start of
            # the window to the right of the last occurrence of 
this character.
            if current_char in char_index_map and char_index_map
[current_char] >= start:
                start = char_index_map[current_char] + 1

            # Update the last seen index of the current character
            char_index_map[current_char] = end

            # Calculate the length of the current substring and 
update max_length if it's longer
            current_length = end - start + 1
```