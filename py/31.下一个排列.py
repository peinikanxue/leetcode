from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        if not nums:
            return []

        i = len(nums) - 1
        pos = -1

        while i > 0:
            
            if pos == -1 and nums[i-1] < nums[i]: # 找到逆序的地方
                pos = i - 1
                i = len(nums) - 1
            
            if pos != -1 and nums[pos] < nums[i]:   # 找到下一个序列的值，交换到pos位置
                nums[pos], nums[i] = nums[i], nums[pos]
                self.reversed(nums, pos + 1, len(nums))  # pos右侧的全部反转
                break

            i -= 1

        if pos == -1:      # 全逆
            nums.reverse()


    def reversed(self, nums, start, end):
        i = 0
        while i != (end - start) // 2:
            nums[start + i], nums[end - i - 1] = nums[end - i - 1], nums[start + i]
            i += 1



if __name__ == "__main__":
    nums_list = [
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 5, 4],
        [1, 2, 4, 3, 5],
        [1, 2, 4, 5, 3],
        [1, 3, 2, 4, 5],
        [1, 3, 2, 5, 4],
        [5, 4, 3, 2, 1],
    ]

    for nums in nums_list:
        Solution().nextPermutation(nums)
        print(nums)