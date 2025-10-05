class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            result = (result * 10) + x % 10
            x = x // 10
        result = result * sign
        if result > 2**31 - 1 or result < -2**31:
            return 0
        return result
