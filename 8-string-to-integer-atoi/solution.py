class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s: return 0

        sign = 1
        result = 0
        i = 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        for c in s[i:]:
            if c not in "0123456789":
                break
            result = result * 10 + int(c)

        result *= sign

        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31

        return result