class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_str = ""

        for r in range(len(strs[0])):
            for s in strs:
                if r == len(s) or strs[0][r] != s[r]:
                    return new_str
            new_str += strs[0][r]

        return new_str