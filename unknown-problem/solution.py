class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}  # Stores the last seen 
index of each character
        max_length = 0
        start = 0  # Start of the sliding window

        for end in range(len(s)):
            current_char = s[end]

            # If the current character is already in 
the map and its last seen index
            # is within the current window (i.e., 
greater than or equal to 'start'),
            # it means we have a repeating 
character. We need to move the start of
            # the window to the right of the last 
occurrence of this character.
            if current_char in char_index_map and 
char_index_map[current_char] >= start:
                start = char_index_map[current_char] 
+ 1

            # Update the last seen index of the 
current character
            char_index_map[current_char] = end

            # Calculate the length of the current 