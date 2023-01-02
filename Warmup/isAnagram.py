from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
		
# Official solution given

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        else:
            smap = {}
            tmap = {}

            for i in range(len(s)):
                smap[s[i]] = smap.get(s[i], 0) + 1
                tmap[t[i]] = tmap.get(t[i], 0) + 1

            for char in s:
                if char not in tmap:
                    return False
                if smap[char] != tmap[char]:
                    return False
            return True
