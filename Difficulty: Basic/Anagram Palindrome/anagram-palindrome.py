from collections import Counter

class Solution:
    def canFormPalindrome(self, s):
        return sum([1 for cnt in Counter(s).values() if cnt & 1 == 1]) <= 1