'''
Longest Substring with At Most K Distinct Characters
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Constraints:

1 <= s.length <= 5 * 10^4
0 <= k <= 50
'''

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return 0
        window = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if len(window) < k:
                window[s[right]] = window.get(s[right], 0) + 1
                longest = max(longest, right - left + 1)
            elif s[right] in window:
                window[s[right]] += 1
                longest = max(longest, right - left + 1)
            else:
                while len(window) == k:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
                window[s[right]] = 1
        return longest
        
# Official solution

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        n = len(s)
        if n * k == 0:
            return 0

        windowStart = 0
        charMap = {}
        maxLen = 0
        
        for windowEnd in range(n):
            char = s[windowEnd]

            if char not in charMap:
                charMap[char] = 1

                while len(charMap) > k:
                    charToRemove = s[windowStart]
                    charMap[charToRemove] -= 1

                    if charMap[charToRemove] == 0:
                        del charMap[charToRemove]

                    windowStart += 1
            else:
                charMap[char] += 1
                
            maxLen = max(maxLen, windowEnd - windowStart + 1)
            
        return maxLen
