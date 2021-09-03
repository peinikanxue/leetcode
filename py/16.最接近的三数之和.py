from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        result = 0
        min_sum = float('inf')
        is_smaller = False    # 回溯条件:是否从更小后变大

        nums.sort()

        for i in range(len(nums)-2):

            L = i + 1
            R = len(nums) - 1
            
            while L < R:
                tmp_sum = nums[i] + nums[L] + nums[R] - target
                if tmp_sum == 0:    # 最小情况
                    return target
                elif abs(tmp_sum) < abs(min_sum):   # 距离更小
                    min_sum = tmp_sum
                    is_smaller = True
                elif is_smaller and abs(tmp_sum) > abs(min_sum):   # 距离更大,小循环里距离变过更小,然后变大了,可以回溯了
                    is_smaller = False
                    break
                    
                    
                if tmp_sum <= 0:    # 负轴方向
                    L += 1
                else:       # 正轴方向
                    R -= 1

            # 去重i
            if i != 0 and nums[i] == nums[i+1]:
                continue
            is_smaller = False
        
        result = min_sum + target
        return result


if __name__ == "__main__":
    test_list = [
        ([-1, 2, 1, -4], 1),
        ([0,1,2], 3),
        ([1,1,1,0], 100),
        ([0,2,1,-3], 1),
        ([1,1,-1,-1,3], -1),
        ([-1,0,1,1,55], 3)
    ]
    

    for test in test_list:
        print(Solution().threeSumClosest(test[0], test[1]))
