class Solution:
    def maxOperations(self, s: str) -> int:
        ops = 0
        ones_count = 0

        i = 0
        while i < len(s):
            if s[i] == '1':
                ones_count += 1
            elif i > 0 and s[i - 1] == '1':
                ops += ones_count
            i += 1

        return ops