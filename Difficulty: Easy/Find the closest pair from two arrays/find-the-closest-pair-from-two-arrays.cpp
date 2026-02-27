class Solution {
  public:
    vector<int> findClosestPair(vector<int> &a, vector<int> &b, int x) {
        // code here
        int i = 0, j = b.size() - 1;
        int d = 1e18, p = 0, q = 0;
        
        while(i < a.size() && j >= 0){
            int s = a[i] + b[j];
            if(abs(s - x) < d){
                d = abs(s - x);
                p = a[i];
                q = b[j];
            }
            if(s > x) j--;
            else i++;
        }
        
        return {p, q};
    }
};