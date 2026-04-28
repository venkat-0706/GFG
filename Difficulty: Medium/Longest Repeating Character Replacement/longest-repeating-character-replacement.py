class Solution:
    def longestSubstr(self, s, k):
        freq = [0] * 26
        
        left = 0
        max_freq = 0
        ans = 0
        
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            freq[idx] += 1
            
            # Most frequent character in current window
            max_freq = max(max_freq, freq[idx])
            
            # Characters to replace = window size - max_freq
            while (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans