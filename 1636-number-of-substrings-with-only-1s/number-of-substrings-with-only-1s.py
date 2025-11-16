class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        i = 0
        subs = 0

        while i < len(s):
            while i < len(s) and s[i] == '1':
                subs += 1
                i += 1

            res += ((subs * (subs + 1) ) // 2)
            subs = 0
            i += 1

        return res % (10 ** 9 + 7)