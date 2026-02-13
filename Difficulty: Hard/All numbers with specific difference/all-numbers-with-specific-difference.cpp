class Solution {
  public:
    int findDigitsSum(int num){
        int ans = 0;
        while(num > 0){
            ans += num% 10;
            num = num / 10;
        }
        return ans;
    }
    int getCount(int n, int d) {
        // code here
        int low = 1;
        int high = n;
        int ans = n+1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(mid - findDigitsSum(mid) < d){
                low = mid+1;
            }
            else{
                ans = mid;
                high = mid-1;
            }
        }
        return n - ans + 1;
    }
};