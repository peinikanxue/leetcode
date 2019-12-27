from utils import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:  # 左顺序
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:                   # 右顺序
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
        
        
if __name__ == "__main__":
    nums_list = [
        [0,1,2,3,4,5,6],
        [4,5,6,7,0,1,2],
        [4,5,6,7,0,1,2],
        [4,5,6,7,0,1,2],
        [4,5,6,7,0,1,2],
        [],
        [1],
        [1, 3],
        [1, 3],
        [1, 3],
        [3,4,5,1,2],
        [4,5,6,7,0,1,2],
    ]
    target_list = [5, 5, 1, 0, 3, 5, 1, 0, 2, 3, 4, 0]

    for nums, target in zip(nums_list, target_list):
        print(Solution().search(nums, target))
