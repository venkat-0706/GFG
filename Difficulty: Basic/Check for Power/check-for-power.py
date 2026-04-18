class Solution:
    def isPower(self, x, y):
        # code here
        if y == 1:
            return True
        if x == 1:
            return y == 1
        res = x
        while res < y:
            res *= x
        return res == y