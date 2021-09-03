from functools import lru_cache

# 动态规划
# class Solution:
#     def stoneGame(self, piles):
#         N = len(piles)

#         @lru_cache(None)
#         def dp(i, j):
#             # The value of the game [piles[i], piles[i+1], ..., piles[j]].
#             if i > j: return 0
#             parity = (j - i - N) % 2
#             if parity == 1:  # first player
#                 return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
#             else:
#                 return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

#         return dp(0, N - 1) > 0


# 数学方法
class Solution:
    def stoneGame(self, piles):
        return True


if __name__ == "__main__":
    piles_list = [
        [5, 3, 4, 5],
        [3, 2, 10, 4],
        [8,9,7,6,7,6],
    ]

    for piles in piles_list:
        print(Solution().stoneGame(piles))