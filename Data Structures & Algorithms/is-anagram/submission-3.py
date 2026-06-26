class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hash_set1 = {}
        hash_set2 = {}

        for i in range(len(s)):
            hash_set1[s[i]] = 1 + hash_set1.get(s[i], 0)
            hash_set2[t[i]] = 1 + hash_set2.get(t[i], 0)
        
        for c in hash_set1:
            if hash_set1[c] != hash_set2.get(c , 0):
                return False
        return True