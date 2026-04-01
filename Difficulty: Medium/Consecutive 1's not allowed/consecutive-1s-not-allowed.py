class Solution:
    def countStrings(self, n):
        if n<3:
            return n+1
        
        a, b = 2, 3  # dp[1], dp[2]
        
        for _ in range(3, n + 1):
            a, b = b, a + b
        
        return b