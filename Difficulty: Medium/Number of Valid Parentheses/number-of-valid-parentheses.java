 class Solution {
    int findWays(int n) {
        if (n % 2 != 0) return 0;   
        
        int k = n / 2;
        long[] dp = new long[k + 1];
        dp[0] = 1;
        for (int i = 1; i <= k; i++) {
            dp[i] = 0;
            for (int j = 0; j < i; j++) {
                dp[i] += dp[j] * dp[i - j - 1];
            }
        }
        return (int) dp[k];
    }
}

