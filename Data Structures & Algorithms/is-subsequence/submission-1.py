class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False 

        ptr_s = 0

        for ch in t:
            if ptr_s < len(s) and s[ptr_s] == ch:
                ptr_s +=1
            
            if ptr_s == len(s):
                return True
        
        return len(s) == ptr_s
        