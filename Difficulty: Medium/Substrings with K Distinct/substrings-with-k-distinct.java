class Solution {
    public int countSubstr(String s, int k) {
        //  code here
        char[] S=s.toCharArray();
        
        return atMostK(S,k)-atMostK(S,k-1);
    }
    
    int atMostK(char[]s ,int k){
        if(k<0)return 0;
         int map[]=new int[26];
         int distinct=0;
         
         int i=0;
         int ans=0;
         for(int j=0;j<s.length;j++){
             int ch=s[j]-'a';
             
             map[ch]++;
             if(map[ch]==1) distinct++;
             
             while(i<=j && distinct>k){
                 int c=s[i]-'a';
                 map[c]--;
                 if(map[c]==0) distinct--;
                 i++;
             }
             
             ans+=(j-i+1);
         }
         return ans;
         
    }
}