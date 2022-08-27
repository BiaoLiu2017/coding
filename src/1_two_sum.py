# 简版：即从一个数组nums中找出和为target的两个数的index，并返回，而且仅有一个答案
'''
两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]



提示：

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
'''
# 解题思路：
# 构建一个字典，开始遍历整个list，每当遇到元素x，就看target-x是否存在于字典中，如果不存在，则将x作为key，x的index作为value放进字典，如果存在即返回结果。
# 时间复杂度为O(n)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, n in enumerate(nums):
            left = target - n
            if left not in dic:
                dic[n] = i
            else:
                return [dic[left], i]
        return []

s = Solution()
print(s.twoSum([2,7,11,15], 9))