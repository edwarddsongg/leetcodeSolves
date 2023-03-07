class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = ["I", "V", "X", "L", "C", "D", "M"]

        tens = 1

        for(i)