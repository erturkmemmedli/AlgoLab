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
