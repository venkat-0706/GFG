class Solution {
  public:
    long long sumXOR(vector<int> &arr) {
        int n = arr.size();
        long long result = 0;

        for(int bit = 0; bit < 32; bit++) {
            long long count1 = 0;

            for(int i = 0; i < n; i++) {
                if(arr[i] & (1 << bit)) {
                    count1++;
                }
            }

            long long count0 = n - count1;

            result += (count1 * count0) * (1LL << bit);
        }

        return result;
    }
};

