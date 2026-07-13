class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0 
        seen = {}
        max_len = 0

        while j < len(s):
            
            if s[j] in seen and seen[s[j]] >= i:
                i = seen[s[j]] + 1
                seen[s[j]] = j

            else:
                seen[s[j]] = j

            l = j - i + 1
            max_len = max(l, max_len)

            j += 1
        
        return max_len
