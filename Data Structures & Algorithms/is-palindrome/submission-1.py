import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        plain_txt = (re.sub(r"[^a-zA-Z0-9]", '', s)).lower()
        if plain_txt[::-1] == plain_txt:
            return True
        return False