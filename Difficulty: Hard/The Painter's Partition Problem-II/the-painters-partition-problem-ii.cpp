class Solution {
  public:
    bool isfeasible(int timee,int k,vector<int>&arr){
        
        int count=1;
        int sum=0;
        for(int i=0;i<arr.size();i++){
            if(sum+arr[i]>timee){
                sum=arr[i];
                count++;
                if(count>k) return false;
            }
            else{
                sum+=arr[i];
            }
        }
        
        return true;
        
        
    }
    int minTime(vector<int>& arr, int k) {
        // code here
        
        int sum=0;
        const int n=arr.size();
        int minn=INT_MIN;
        for(int i=0;i<n;i++){
            sum+=arr[i];
            minn=max(minn,arr[i]);
        }
        
        int i=minn;
        int j=ceil((double)n/k)*minn;
        
        while(i<j){
            
            int mid=i+(j-i)/2;
            if(isfeasible(mid,k,arr)){
                j=mid;
            }
            else{
                i=mid+1;
            }
            
        }
        
        return j;
    }
};