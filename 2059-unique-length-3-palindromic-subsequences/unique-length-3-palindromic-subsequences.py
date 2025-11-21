class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        
        for char in set(s):
            first = s.index(char)
            last = s.rindex(char)
            
            if first < last:
                res += len(set(s[first+1 : last]))
        
        return res