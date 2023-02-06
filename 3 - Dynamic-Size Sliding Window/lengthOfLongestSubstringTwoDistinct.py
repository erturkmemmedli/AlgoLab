'''
Longest Substring with At Most Two Distinct Characters
Given a string s, return the length of the longest 
substring that contains at most two distinct characters. 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 
Constraints:

1 <= s.length <= 10^5
s consists of English letters.
'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        window = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if len(window) < 2:
                window[s[right]] = window.get(s[right], 0) + 1
                longest = max(longest, right - left + 1)
            elif s[right] in window:
                window[s[right]] += 1
                longest = max(longest, right - left + 1)
            else:
                while len(window) == 2:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    left += 1
                window[s[right]] = 1
        return longest

# Official solution

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n

        windowStart = 0
        charMap = {}
        maxLen = 0
        
        for windowEnd in range(n):
            char = s[windowEnd]

            if char not in charMap:
                charMap[char] = 1

                while len(charMap) > 2:
                    charToRemove = s[windowStart]
                    charMap[charToRemove] -= 1

                    if charMap[charToRemove] == 0:
                        del charMap[charToRemove]

                    windowStart += 1
            else:
                charMap[char] += 1
                
            maxLen = max(maxLen, windowEnd - windowStart + 1)
            
        return maxLen
