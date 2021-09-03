from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         '''
#             a+b=-c
#         '''

#         if nums == []:
#             return []
        
#         result_list = []

#         query_dict = dict(zip(nums, [0]*len(nums))) # 查询表
#         skip_a_dict = {}    # 记录大循环已用过的a
#         skip_bc_dict = {}   # 记录小循环已用过的b,c

#         # 构建查询表
#         for num in nums:
#             query_dict[num] += 1
        
#         # 查询满足的数，并添加到列表
#         for i in range(len(nums)):
#             a = nums[i]

#             if query_dict[a] > 0:
#                 for j in range(i+1, len(nums)):
#                     b = nums[j]
#                     c = -(a+b)

#                     # 使用计数
#                     query_dict[a] -= 1
#                     query_dict[b] -= 1

#                     # 添加满足条件的列表
#                     if c in query_dict and query_dict[c] > 0 and b not in skip_a_dict and b not in skip_bc_dict:
#                         result = [a, b, c]
#                         result.sort()
#                         result_list.append(result)

#                         # 暂时记下小循环里使用的数
#                         skip_bc_dict[b] = True
#                         skip_bc_dict[c] = True
                    
#                     # 使用计数恢复
#                     query_dict[a] += 1
#                     query_dict[b] += 1
            
#             # 消除大循环使用过的数
#             query_dict[a] = 0
#             skip_a_dict[a] = True
#             skip_bc_dict = {}

#         return result_list


# 题解
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 特殊值
        if nums == [] or len(nums) < 3:
            return []

        nums.sort() # 排序便于回溯

        L = 1
        R = len(nums) - 1
        tmp_sum = 0
        result_list = []

        for i in range(len(nums)-2):
            if nums[i] > 0: # 如果当前数字大于0，三个数必然无法满足
                break
            if i > 0 and nums[i] == nums[i-1]:  # 去重
                continue

            L = i + 1
            R = len(nums) - 1
            while L < R:
                tmp_sum = nums[i] + nums[L] + nums[R]
                if tmp_sum == 0:
                    result = [nums[i], nums[L], nums[R]]
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
    nums_list = [
        [-1, 0, 1, 2, -1, -4], # [-4, -1, -1, 0, 1, 2]
        [],
        [-1,0,1],
        [-1,0,1,0],
        [-1,0,1,2,-1,-4],
        [-2,0,0,2,2],
        [3,0,-2,-1,1,2],
        [0,0,0,0],
    ]
    for nums in nums_list:
        print(Solution().threeSum(nums))