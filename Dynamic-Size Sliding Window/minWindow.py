class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s): return ""
        minLength = float("inf")
        substring = ""
        left = 0
        tMap = {}
        for char in t:
            tMap[char] = 1 if char not in tMap else tMap[char] + 1
        sMap = {}
        for right, char in enumerate(s):
            if char not in tMap:
                continue
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char] += 1
            while len(sMap) == len(tMap) and all(tMap[key] <= sMap[key] for key in tMap):
                if minLength > right - left + 1:
                    minLength = right - left + 1
                    substring = s[left: right + 1]
                if s[left] in sMap:
                    sMap[s[left]] -= 1
                    if sMap[s[left]] == 0:
                        del sMap[s[left]]
                left += 1
        return substring

# Official solution

class Solution:
    def minWindow(self, s, t):
        freq = {}
        for char in t:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1

        matched = 0
        minStart = 0
        minLength = float("inf")
        windowStart = 0

        for windowEnd in range(len(s)):
            char = s[windowEnd]

            if char in freq:
                freq[char] -= 1

                if freq[char] == 0:
                    matched += 1

            while matched == len(freq):
                windowSize = windowEnd - windowStart + 1
                if windowSize < minLength:
                    minLength = windowSize
                    minStart = windowStart

                remove = s[windowStart]

                if remove in freq:
                    if freq[remove] == 0:
                        matched -= 1
                    freq[remove] += 1
                windowStart += 1

        if minLength == float("inf"):
            return ""
        return s[minStart : minStart + minLength]
