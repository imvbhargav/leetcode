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
                    