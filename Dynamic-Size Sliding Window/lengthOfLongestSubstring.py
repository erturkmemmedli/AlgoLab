class Solution:
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        left = 0
        length = 0
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
                length = max(length, len(hashmap))
            else:
                hashmap[char] += 1
                while hashmap[char] != 1:
                    hashmap[s[left]] -= 1
                    if hashmap[s[left]] == 0:
                        del hashmap[s[left]]
                    left += 1
        return length
