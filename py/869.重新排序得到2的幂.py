# class Solution:
#     def reorderedPowerOf2(self, N: int) -> bool:

#         # 获取1~10^10 -> 2^0~2^30的查找表
#         def make_dict():
#             l1 = [x for x in range(30)]
#             l1 = list(map(lambda x: 2**x, l1))
#             d = {}

#             for ll1 in l1:
#                 count = 0
#                 l2 = []
#                 while ll1 > 0:
#                     l2.append(ll1 % 10)
#                     ll1 //= 10
#                     count += 1
#                 if count not in d:
#                     d[count] = []
#                 d[count].append(l2)
#             return d
        
#         my_dict = make_dict()
        
#         # 计数
#         M = N
#         count = 0
#         while M > 0:
#             count += 1
#             M //= 10
#         # 查表
#         if count in my_dict:
#             table = my_dict[count]
#         else:
#             # print('不存在表')
#             return False
#         # 有多个表
#         def query(table, N):
#             while N > 0:
#                 val = N % 10
#                 N //= 10
#                 if val in table:
#                     table.remove(val)
#                 else:       # 不成立
#                     return False
#             return True     # 全部遍历完，成立
#         if isinstance(table[0], list):
#             for t in table:
#                 if query(t, N):
#                     return True
#         # 只有一个表
#         else:
#             if query(table, N):
#                 return True
#         # 全部表查完，没有满足的
#        return False


# 题解
from collections import Counter
class Solution(object):
    def reorderedPowerOf2(self, N):
        count = Counter(str(N))
        return any(count == Counter(str(1 << b)) for b in range(31))


if __name__ == "__main__":
    N_list = [1, 10, 16, 24, 46]

    for N in N_list:
        print(Solution().reorderedPowerOf2(N))