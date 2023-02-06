'''
Find K-Length Substrings With No Repeated Characters
Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
 

Constraints:

1 <= s.length <= 10^4
s consists of lowercase English letters.
1 <= k <= 10^4
'''

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
