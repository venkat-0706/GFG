class Solution {
public:
    int countSubset(vector<int>& arr, int k) {
        int n = arr.size();
        int mid = n / 2;

        vector<long long> leftSums, rightSums;

        // Generate sums of left half
        for (int mask = 0; mask < (1 << mid); mask++) {
            long long sum = 0;
            for (int i = 0; i < mid; i++) {
                if (mask & (1 << i))
                    sum += arr[i];
            }
            leftSums.push_back(sum);
        }

        // Generate sums of right half
        for (int mask = 0; mask < (1 << (n - mid)); mask++) {
            long long sum = 0;
            for (int i = 0; i < n - mid; i++) {
                if (mask & (1 << i))
                    sum += arr[mid + i];
            }
            rightSums.push_back(sum);
        }

        sort(rightSums.begin(), rightSums.end());

        int count = 0;
        for (long long s : leftSums) {
            long long need = k - s;
            count += upper_bound(rightSums.begin(), rightSums.end(), need)
                   - lower_bound(rightSums.begin(), rightSums.end(), need);
        }

        return count;
    }
};