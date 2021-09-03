from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # 特殊值
        if nums == [] or len(nums) < 4:
            return []

        nums.sort() # 排序便于回溯

        L = 1
        R = len(nums) - 1
        tmp_sum = 0
        result_list = []


        for i in range(len(nums)-3):
            
            if i > 0 and nums[i] == nums[i-1]:  # 去重
                continue

            for j in range(i+1, len(nums)-2):
                if j > 1 and j-i > 1 and nums[j] == nums[j-1]:  # 去重
                    continue

                L = j + 1
                R = len(nums) - 1
                while L < R:
                    tmp_sum = nums[i] + nums[j] + nums[L] + nums[R] - target
                    if tmp_sum == 0:
                        result = [nums[i], nums[j], nums[L], nums[R]]
                        result.sort()
                        result_list.append(result)

                        # 去重
                        while(L<R and nums[L] == nums[L+1]):
                            L += 1
                        while(L<R and nums[R] == nums[R-1]):
                            R -= 1
                        L += 1
                        R -= 1
                    elif tmp_sum < 0:
                        L += 1
                    else:
                        R -= 1
        
        return result_list


if __name__ == "__main__":
    test_list = [
        ([1, 0, -1, 0, -2, 2], 0),
        ([0,0,0,0], 0),
        ([0,0,0,0], 1),
        ([-1,0,1,2,-1,-4], -1),
        ([-3,-2,-1,0,0,1,2,3], 0),
        ([0,4,-5,2,-2,4,2,-1,4], 12),
    ]
    for test in test_list:
        print(Solution().fourSum(test[0], test[1]))