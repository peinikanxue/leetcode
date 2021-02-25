from utils import *

import collections

class Solution(object):
    def cutOffTree(self, forest):
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for _, tr, tc in trees:
            d = dist(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans

def dist(forest, sr, sc, tr, tc):
    R, C = len(forest), len(forest[0])
    queue = collections.deque([(sr, sc, 0)])
    seen = {(sr, sc)}
    while queue:
        r, c, d = queue.popleft()
        if r == tr and c == tc:
            return d
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if (0 <= nr < R and 0 <= nc < C and
                    (nr, nc) not in seen and forest[nr][nc]):
                seen.add((nr, nc))
                queue.append((nr, nc, d+1))
    return -1



if __name__ == "__main__":
    forests = [
        # [
        #     [1, 2, 3, 4],
        #     [0, 7, 5, 6],
        #     [11, 10, 8, 9],
        # ],
        # [
        #     [1, 2, 3, 4],
        #     [0, 7, 5, 6],
        #     [11, 0, 8, 9],
        # ],
        [
            [54581641,64080174,24346381,69107959],
            [86374198,61363882,68783324,79706116],
            [668150  ,92178815,89819108,94701471],
            [83920491,22724204,46281641,47531096],
            [89078499,18904913,25462145,60813308]
        ],
        [
            [9, 12, 5, 14],
            [17, 11, 13, 15],
            [2, 20, 19, 21],
            [16, 4, 7, 8],
            [18, 3, 6, 10]
        ],
    ]

    for forest in forests:
        print(Solution().cutOffTree(forest))
