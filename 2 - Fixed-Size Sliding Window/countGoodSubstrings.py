class Solution:
    def countGoodSubstrings(self, s):
        distinct = 0
        for i in range(len(s) - 2):
            w = s[i:i+3]
            if w[0] != w[1] and w[0] != w[2]  and w[1] != w[2]:
                distinct += 1
        return distinct
      
# Official solution

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
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
