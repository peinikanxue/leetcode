
# 题解
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        T = [[0] * k for k in range(1, 102)]
        T[0][0] = poured

        for row in range(query_row + 1):
            for col in range(row + 1):
                half = (T[row][col] - 1.0) / 2
                if half > 0:
                    T[row+1][col] += half
                    T[row+1][col+1] += half
        return min(1, T[query_row][query_glass])


if __name__ == "__main__":
    print(Solution().champagneTower(2, 1, 1))
