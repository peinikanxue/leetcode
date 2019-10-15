from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        cur_area = 0

        start = 0
        end = len(height) - 1

        while start < end:
            # 计算面积
            cur_area = min(height[start], height[end]) * (end - start)
            if cur_area >= max_area:
                max_area = cur_area
            # 前进
            if height[start] < height[end]: # 左边的矮，左边向右进
                start += 1
            else:
                end -= 1
        
        return max_area


if __name__ == "__main__":
    height_list = [
        [1,8,6,2,5,4,8,3,7],
        [1,2,4,3],
        [1,3,2,5,25,24,5],
    ]
    for height in height_list:
        print(Solution().maxArea(height))