# 6. Zigzag Conversion

## Problem

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R


And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


 
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"


Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I


Example 3:

Input: s = "A", numRows = 1
Output: "A"


 
Constraints:


	1 <= s.length <= 1000
	s consists of English letters (lower-case and upper-case), ',' and '.'.
	1 <= numRows <= 1000

## Solution

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        def firstMethod():
            # If only row allowed or if the string is shorter than
            # the row count return the original string
            if numRows == 1 or numRows > len(s):
                return s
            
            res = ""

            # Keep looping through the rows
            for r in range(numRows): 
                 # Jump to the next number according to number of rows
                increment = 2 * (numRows - 1)
                
                # Loop from the row index to the last char of
                # string with calculated increment
                for i in range(r, len(s), increment):
                    res += s[i]

                    # If now is not first or last, then get the additional char
                    # within the bounds
                    if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
                        res += s[i + increment - 2 * r]
            return res

        def secondMethod():
            # If only row allowed or if the string is shorter than
            # the row count return the original string
            if numRows == 1 or numRows > len(s):
                return s
            
            index, direction = 0, -1
            res_rows = [''] * numRows

            # Loop through the string
            for char in s:
                res_rows[index] += char

                # Change the direction if reached first row or last row
                if index == 0 or index == numRows - 1:
                    direction *= -1

                # Change row index based on direction
                index += direction
    
            # Join the array to a string
            return ''.join(res_rows)

        return secondMethod()
```
