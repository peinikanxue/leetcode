from utils import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:    # 边界：没有值
            return 0

        count = 1   # 计数
        index = 1   # 记录交换的位置

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += 1
                nums[index] = nums[i]   # 移动值
                index += 1
        return count


if __name__ == "__main__":
    nums_list = [
        [],
        [0, 0],
        [0, 1],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
    ]

    for nums in nums_list:
        print(Solution().removeDuplicates(nums), end=' - ')
        print(nums)
