class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]

        for n in nums:
            tmp = dp[:]

            for i in range(3):
                rem = (i + n) % 3
                tmp[rem] = max(tmp[rem], dp[i] + n)

            dp = tmp

        return dp[0]