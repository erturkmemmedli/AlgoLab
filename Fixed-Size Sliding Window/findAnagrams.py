class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        k = len(p)
        anagrams = []
        frequency = {}
        headWindow = 0
        for char in p:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
        for i, char in enumerate(s):
            if char in frequency:
                frequency[char] -= 1
                if not frequency[char]:
                    del frequency[char]
            else:
                frequency[char] = -1
            if i == k - 1:
                if not frequency:
                    anagrams.append(0)
            elif i >= k:
                if s[headWindow] not in frequency:
                    frequency[s[headWindow]] = 1
                else:
                    frequency[s[headWindow]] += 1
                    if not frequency[s[headWindow]]:
                        del frequency[s[headWindow]]
                if not frequency:
                    anagrams.append(headWindow + 1)
                headWindow += 1
        return anagrams
      
# Official solution given
      
class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        pMap = {}
        for char in p:
            if char not in pMap:
                pMap[char] = 1
            else:
                pMap[char] += 1
        sMap = {}
        k = len(p)
        result = []

        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 1
            else:
                sMap[s[i]] += 1
            if i >= k:
                if sMap[s[i - k]] == 1:
                    del sMap[s[i - k]]
                else:
                    sMap[s[i - k]] -= 1
            if pMap == sMap:
                result.append(i - k + 1)

        return result
