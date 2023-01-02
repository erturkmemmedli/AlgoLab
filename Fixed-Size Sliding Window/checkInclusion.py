class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        k = len(s1)
        map1 = {}
        for char in s1:
            if char not in map1:
                map1[char] = 1
            else:
                map1[char] += 1
        map2 = {}
        for i, char in enumerate(s2):
            if char not in map2:
                map2[char] = 1
            else:
                map2[char] += 1
            if i >= k:
                map2[s2[i - k]] -= 1
                if not map2[s2[i - k]]:
                    del map2[s2[i - k]]
            if map1 == map2:
                return True
        return False
        
# Official solution given

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        pMap = {}
        for char in s1:
            if char not in pMap:
                pMap[char] = 1
            else:
                pMap[char] += 1
        sMap = {}
        k = len(s1)
        for i in range(len(s2)):
            if s2[i] not in sMap:
                sMap[s2[i]] = 1
            else:
                sMap[s2[i]] += 1
            if i >= k:
                if sMap[s2[i - k]] == 1:
                    del sMap[s2[i - k]]
                else:
                    sMap[s2[i - k]] -= 1
            if pMap == sMap:
                return True

        return False
