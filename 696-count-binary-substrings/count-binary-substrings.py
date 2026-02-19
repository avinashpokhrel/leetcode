class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr_sym = s[0]
        cnt = 1
        intr_arr = []
        i = 1
        while(i < len(s)):

            if(s[i] == curr_sym):
                cnt += 1
            else:
                intr_arr.append(cnt)
                curr_sym = s[i]
                cnt = 1

            i += 1
        
        intr_arr.append(cnt)
        ans = 0

        i = 0
        while(i < len(intr_arr) - 1):
            ans += min(intr_arr[i], intr_arr[i + 1])
            i += 1

        return ans