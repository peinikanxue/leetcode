from utils import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]
        if nums == []:
            return 0
        dp.append(nums[0])

        i = 0
        for i in range(2, len(nums)+1):
            dp.append(max(dp[i-1], dp[i-2]+nums[i-1]))
        return dp[-1]


if __name__ == "__main__":
    nums_list = [
        [1,2,3,1],
        [2,7,9,3,1],
        [2,1,1,2],
        [2,4,8,9,9,3],
    ]

    for nums in nums_list:
        print(Solution().rob(nums))