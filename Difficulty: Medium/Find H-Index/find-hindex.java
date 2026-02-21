class Solution {
    public int hIndex(int[] citations) {
        if (citations == null || citations.length == 0) return 0;
        int n = citations.length;
        int[] buckets = new int[n + 1];
        for (int c : citations) {
            if (c >= n) buckets[n]++;
            else buckets[c]++;
        }

        int papers = 0; 
        for (int i = n; i >= 0; i--) {
            papers += buckets[i];
            if (papers >= i) return i; 
        }
        return 0; 
    }
}

