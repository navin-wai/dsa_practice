class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f , s = 0 , 0
        output = ""
        while f < len(word1) and s < len(word2):
            output += word1[f]
            output += word2[s]
            f += 1 
            s += 1
        while f < len(word1):
            output += word1[f]
            f+= 1
        while s < len(word2):
            output += word2[s]
            s+= 1
        return output 