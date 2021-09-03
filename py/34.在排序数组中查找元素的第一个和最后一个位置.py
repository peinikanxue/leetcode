from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        l_limt = -1
        r_limt = -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                l_limt = self.search_l(nums, target, 0, m)            # 搜索左边的边界
                r_limt = self.search_r(nums, target, m, len(nums) - 1)# 搜索右边的边界
                break
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        return [l_limt, r_limt]


    def search_l(self, nums, target, l, r):
        m = (l + r) // 2
        
        if nums[m] == target and (m == 0 or nums[m-1] < target):    # 左边
            return m
        
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
        return self.search_l(nums, target, l, r)


    def search_r(self, nums, target, l, r):
        m = (l + r) // 2

        if nums[m] == target and (m == len(nums) - 1 or nums[m+1] > target):    # 右边
            return m
        
        if nums[m] <= target:
            l = m + 1
        else:
            r = m - 1
        return self.search_r(nums, target, l, r)



if __name__ == "__main__":
    nums_list = [
        [5,7,7,8,8,10],
        [5,7,7,8,8,10],
        [1],
        [0, 1],
        [0, 1],
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
        [2, 2],
        [0,0,0,1,2,3],
        [0,1,2,3,3,3],
    ]

    target_list = [8, 6, 1, 0, 1, 0, 1, 2, 2, 0, 3]

    for nums, target in zip(nums_list, target_list):
        print(Solution().searchRange(nums, target))

