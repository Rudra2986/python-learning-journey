class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_s = ""
        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch
        clean.ignorecase()

        for i in range(len(clean) - 1, -1, -1):
            reverse_s += clean[i]
        if reverse_s == clean :
            return True
        return False