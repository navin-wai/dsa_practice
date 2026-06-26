import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        s = re.sub(r"[!@#$%^&*(),.;'\[\]/?<>:\":=-]", "", s)
        s = s.replace(" " , "")
        print(s)
        ptr1 = 0 
        ptr2 = len(s) - 1
        
        while ptr1 <= ptr2:
            if s[ptr1] != s[ptr2]:
                return False
            else:
                ptr1 += 1
                ptr2 -= 1
        return True