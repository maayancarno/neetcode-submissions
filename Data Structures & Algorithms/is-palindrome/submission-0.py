class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_formatted = "".join(ch for ch in s if ch.isalnum()).lower()
        left = 0
        right = len(s_formatted)- 1
        while left < right:
            if s_formatted[left] != s_formatted[right]:
                return False
            left += 1
            right -= 1
        return True
            