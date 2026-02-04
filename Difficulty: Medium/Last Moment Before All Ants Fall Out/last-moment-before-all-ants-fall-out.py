class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        to_left = max(left,default=0)
        to_right = min(right,default=n)
        return max(n-to_right,to_left)