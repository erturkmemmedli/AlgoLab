class Solution:
    def numKLenSubstrNoRepeats(self, s, k):
        frequency = {}
        count = 0
        for i, char in enumerate(s):
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
            if i >= k:
                frequency[s[i - k]] -= 1
                if not frequency[s[i - k]]:
                    del frequency[s[i - k]]
            if len(frequency) == k:
                count += 1
        return count
        
# Official solution

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = 0
        freq = {}
        windowStart = 0

        for windowEnd in range(len(s)):
            if s[windowEnd] not in freq:
                freq[s[windowEnd]] = 1
            else:
                freq[s[windowEnd]] += 1

            if windowEnd >= k - 1:
                if len(freq) == k:
                    count += 1
                if freq[s[windowStart]] == 1:
                    del freq[s[windowStart]]
                else:
                    freq[s[windowStart]] -= 1

                windowStart += 1

        return count
