class Solution:
    def isPallindrome(self, N):
        # code here
        N=bin(N)[2:]
        if N==N[::-1]:
            return 1
        return 0