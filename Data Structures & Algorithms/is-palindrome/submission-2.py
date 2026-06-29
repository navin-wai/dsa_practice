class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for n in s:
            if n.isalnum():
                new_str += n.lower()
        return new_str == new_str[::-1]