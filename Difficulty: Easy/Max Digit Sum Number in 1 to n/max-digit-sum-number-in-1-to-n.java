class Solution {
    public int findMax(int n) {
        if (n <= 9) return n;

        long maxSum = digitSum(n);
        int result = n;

        long temp = n;
        long multiplier = 1;

        while (temp > 0) {
            long candidate = (temp - 1) * multiplier + (multiplier - 1);
            long currentSum = digitSum(candidate);

            if (currentSum > maxSum || (currentSum == maxSum && candidate > result)) {
                maxSum = currentSum;
                result = (int) candidate;
            }

            temp /= 10;
            multiplier *= 10;
        }

        return result;
    }

    private long digitSum(long n) {
        long sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}