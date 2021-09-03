from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        cycle = length // 2 - 1
        
        # 取出2数组中前面多余的元素
        for i in range(cycle):
            if nums2 == [] or (nums1 != [] and nums2 != [] and nums1[0] < nums2[0]):
                nums1.pop(0)
            else:
                nums2.pop(0)

        # 如果2个数组总共只有1个元素，直接返回
        if length == 1:
            return nums1[0] if nums1 != [] else nums2[0]
        
        # 元素多于1个的情况
        result = []
        for i in range(2):
            if nums2 == [] or (nums1 != [] and nums2 != [] and nums1[0] < nums2[0]):
                result.append(nums1.pop(0))
            else:
                result.append(nums2.pop(0))
        
        if length % 2 == 0:
            return sum(result) / 2
        else:
            return result[1]
            
if __name__ == "__main__":
    nums_list = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([], [1]),
        ([2], [])
        ]
    for nums1, nums2 in nums_list:
        print(Solution().findMedianSortedArrays(nums1, nums2))