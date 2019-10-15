from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            key = nums[i]
            if key not in map:  # 如果前面没有这个键
                map[key] = []
            map[key].append(i)
            
        for i in range(len(nums)):
            result = target - nums[i]
            if result in map:   # 如果键存在
                for j in range(len(map[result])):
                    if map[result][j] != i:     # 元素未使用过
                        return [i, map[result][j]]

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    print(Solution().twoSum(nums))