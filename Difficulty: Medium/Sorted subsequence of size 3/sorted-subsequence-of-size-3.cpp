class Solution {
  public:
    vector<int> find3Numbers(vector<int> &arr) {
        // Code here
        int tempSmall = INT_MAX;
        int fSmall = INT_MAX;
        int sSmall = INT_MAX;
        
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] > sSmall) {
                return {fSmall, sSmall, arr[i]};
            }
            else if (arr[i] > fSmall) {
                sSmall = arr[i];
            }
            else if (arr[i] > tempSmall) {
                fSmall = tempSmall;
                sSmall = arr[i];
            }
            else {
                tempSmall = arr[i];
            }
        }
        
        return {};
    }
};