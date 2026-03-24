class Solution {
    public boolean canFinish(int n, int[][] pre) {
        // code here
        if(n == 1) return true;
        
        Set<Integer> set = new HashSet<>();
        
        for(int i=0; i<pre.length; i++){
            set.add(pre[i][1]);
        }
        
        for(int i=0; i<pre.length; i++){
           
           if(!set.contains(pre[i][0])) return true;
        }
        
        return false;
    }
}

