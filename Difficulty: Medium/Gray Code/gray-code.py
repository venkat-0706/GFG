class Solution:
    def graycode(self,n):
        return [bin(num ^ (num >> 1))[2:].rjust(n, "0") for num in range(2**n)]