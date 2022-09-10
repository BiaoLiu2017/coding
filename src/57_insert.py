'''
57. 插入区间

给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。



示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

示例 3：

输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]

示例 4：

输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]

示例 5：

输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]
'''
from typing import List
# 思路一：跟56_merge思路是一样的
'''
执行结果：通过
执行用时：28 ms, 在所有 Python3 提交中击败了99.44% 的用户
内存消耗：16.7 MB, 在所有 Python3 提交中击败了27.72% 的用户
通过测试用例：156 / 156
炫耀一下:'''
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         res = [intervals[0]]
#         left = intervals[0]
#         for right in intervals[1:]:
#             if left[1] >= right[0]:
#                 if left[1] < right[1]:
#                     left = [left[0], right[1]]
#                     res[-1] = left
#                 # print(res)
#             else:
#                 left = right
#                 res.append(left)
#         return res
#
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         is_insert = False
#         for i, w in enumerate(intervals):
#             if w[0] > newInterval[0]:
#                 intervals.insert(i, newInterval)
#                 is_insert = True
#                 break
#         if not is_insert:
#             intervals.append(newInterval)
#         return self.merge(intervals)

# 思路二：
# 依次比较，找到有overlap的左侧元素和右侧元素，然后将有overlap的进行merge，然后再合并，速度应该更快
'''
执行结果：通过
执行用时：28 ms, 在所有 Python3 提交中击败了99.44% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了9.54% 的用户
通过测试用例：156 / 156'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []#分别放overlap左侧和右侧的interval
        merge_interval = []#merge ovelapping intervals
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:#无overlap，为左侧interval
                left.append(interval)
            elif interval[0] > newInterval[1]:#无overlap，为右侧interval
                right += intervals[i:]
                break
            else:#有overlap
                merge_interval.append(interval)
        if merge_interval:
            merge_interval = [[min(merge_interval[0][0], newInterval[0]), max(merge_interval[-1][1], newInterval[1])]]
        else:
            merge_interval = [newInterval]
        return left + merge_interval + right

s = Solution()
print(s.insert([[1,3],[6,9]], [2,5]))