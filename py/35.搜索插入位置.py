from utils import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:   # 等于该值
                return m
            # 目标值大于等于左边的小于右边的
            if nums[m] < target and m+1 < len(nums) and target < nums[m+1]:
                return m + 1
            elif m == len(nums)-1 and target > nums[m]:  # 右边界
                return m + 1
            elif m == 0 and target <= nums[m]:            # 左边界
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1


if __name__ == "__main__":
    nums_list = [
        [1,3,5,6],
        [1,3,5,6],
        [1,3,5,6],
        [1,3,5,6],
        [1],
        [1],
    ]
    target_list = [5, 2, 7, 0, 2, 0]

    for nums, target in zip(nums_list, target_list):
        print(Solution().searchInsert(nums, target))

