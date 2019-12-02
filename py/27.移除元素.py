from utils import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0

        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                continue
            i += 1
        return len(nums)

if __name__ == "__main__":
    nums_list = [
        [],
        [3, 2, 2, 3],
    ]
    val_list = [1, 3]

    for nums, val in zip(nums_list, val_list):
        print(Solution().removeElement(nums, val), end=' - ')
        print(nums)