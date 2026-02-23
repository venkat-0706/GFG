class Solution {
  public:
    int equalSumSpan(vector<int> &a1, vector<int> &a2) {
        int n = a1.size();
        for(int i = 0;i<n;i++){
            a1[i] = a1[i]-a2[i];
        }
        map<int,int> mp;
        int sum = 0, len = 0;
        for(int i = 0;i<n;i++){
            sum+=a1[i];
            if(sum == 0){
                len = max(len, i+1);
            }
            
            auto it = mp.find(sum);
            if(it != mp.end()){
                len = max(len, i-it->second);
            }
            else{
                mp[sum] = i;
            }
        }
        return len;
    }
};