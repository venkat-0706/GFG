class Solution {
  public:
    int findMinDiff(vector<int>& a, int m) {
        sort(a.begin(), a.end());
        int n = a.size();
        int i = 0;
        int ans = INT_MAX;
        while (i+m-1 < n) {
            int mini = a[i];
            int maxi = a[i+m-1];
            ans = min(ans, maxi-mini);
            i++;
        }
        return ans;
    }
};