class Solution:
    def smallestSubstring(self, s):
        # code here
        l = r = 0
        freq = {}
        ans = float('inf')
        
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            while len(freq) == 3:
                ans = min(ans, r-l+1)
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            
        return ans if ans != float('inf') else -1