class Solution:
    def totalWays(self, arr, target):
        total_sum = sum(arr)
        
        if abs(target) > total_sum:
            return 0
            
        if(target + total_sum) % 2 != 0:
            return 0
            
        subset_sum  = (target + total_sum) // 2
        
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_sum]