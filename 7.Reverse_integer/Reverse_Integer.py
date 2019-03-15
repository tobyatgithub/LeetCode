"""
Given a 32-bit signed integer, reverse digits of an integer.

E.g.1:
Input: 123
Output: 321

E.g.2:
Input: -123
Output: -321

E.g.3:
Input: 120
Output: 21

"""


class Solution(object):
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        deappreciated.
        """
        # 1. 32 bit restriction
        if (x > 2**31-1) or (x < -2**31) or (x == 0):
            return 0

        # 2. idea of reverse:
        # int -> str (reserve sign) -> reverse -> 
        # remove all 0 on the left
        sign = ""
        if x < 0:
            sign = "-"

        out = str(abs(x))[::-1]
        
        i = 0
        while i < len(out) and out[i] == '0':
            i += 1

        out = sign + out[i:]
        return int(out)

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # it turns out that the 0 check is not necessary as int()
        # will take care of it.
        
        Neg = False
        if x < 0:
            Neg = True

        out = int(str(abs(x))[::-1])
        if Neg:
            out *= -1
        
        if abs(out) > (2**31 - 1):
            return 0
        return out

