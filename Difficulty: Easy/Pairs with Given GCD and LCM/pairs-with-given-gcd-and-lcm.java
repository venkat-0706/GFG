class Solution {
    public int pairCount(int x, int y) {
        if (y % x != 0) {
            return 0;
        }

        int n = y / x;
        int distinctPrimes = 0;

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                distinctPrimes++;

                while (n % i == 0) {
                    n /= i;
                }
            }
        }

        // Remaining prime factor
        if (n > 1) {
            distinctPrimes++;
        }

        return 1 << distinctPrimes;
    }
}