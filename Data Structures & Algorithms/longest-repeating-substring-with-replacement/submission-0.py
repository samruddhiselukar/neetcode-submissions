class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen, maxfreq = 0, 0
        freq = defaultdict(int)
        l, r = 0, 0

        while r < len(s):
            freq[s[r]] += 1
            maxfreq = max(maxfreq, freq[s[r]])
            size = r - l + 1
            changes = size - maxfreq

            if changes > k:
                freq[s[l]] -= 1
                l += 1

                size = r - l + 1
                changes = size - maxfreq

            else:
                maxlen = max(maxlen, r - l + 1)

            r += 1

        return maxlen


        