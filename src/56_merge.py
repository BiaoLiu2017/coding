'''
56. 合并区间

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。



示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''
from typing import List

# 思路一：
# 先排序，复杂度为O(NlogN)，然后第一个和第二个比较，如果重叠则merge，否则从下一个开始继续往后比较。复杂度为O(N)
'''
执行结果：通过
执行用时：32 ms, 在所有 Python3 提交中击败了99.94% 的用户
内存消耗：17.9 MB, 在所有 Python3 提交中击败了51.03% 的用户
通过测试用例：170 / 170'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda k: k[0])#starti进行排序
        res = [intervals[0]]
        left = intervals[0]
        for right in intervals[1:]:
            if left[1] >= right[0]:
                if left[1] < right[1]:
                    left = [left[0], right[1]]
                    res[-1] = left
                # print(res)
            else:
                left = right
                res.append(left)
        return res

s = Solution()
print(s.merge([[1,4],[0,2],[3,5]]))


