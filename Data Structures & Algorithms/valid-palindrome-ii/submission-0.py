class Solution:
    def validPalindrome(self, s: str) -> bool:
        ptr = 0
        check = ""

        if s == s[::-1]:
            return True
        while ptr != len(s):
            for r in range(len(s)):
                if r == ptr:
                    continue
                check += s[r]
            ptr += 1
            if check == check[::-1]:
                return True
            else:
                check = ""
        return False 