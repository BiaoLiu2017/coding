'''
三数之和

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：

输入：nums = [0,1,1]
输出：[]

示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]



提示：

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105


'''
# 解题思路1，暴力搜索,O(n^3)：
# 三重循环,而且由于需要去重，所以实际速度极慢，计算量是不可接受的。
# from typing import List
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
#         return list(res)

# 解题思路2，利用字典,O(n^2):
# 两重循环，内层采取字典；
'''
执行结果： 通过
执行用时：3648 ms, 在所有 Python3 提交中击败了9.77% 的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了96.70% 的用户
通过测试用例：311 / 311
优势是内存消耗小，但耗时依然太长。
'''
# from typing import List
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         for i in range(len(nums)):
#             left_set = set()
#             for j in range(i+1, len(nums)):
#                 if -nums[j] - nums[i] in left_set:
#                     res.add(tuple(sorted([nums[i], nums[j], -nums[i]-nums[j]])))
#                 else:
#                     left_set.add(nums[j])
#         return list(res)

# 解题思路3（排序+双指针，并且加上跳跃相同数值，避免后续去重的问题）
# 先从小到大排序O（nlogn），然后指定最左边索引i，双指针，左指针j指向i+1，右指针指向n-1，判断是否和为0，
# 若是则记录结果，并且左指针向右移动直到数值变化，右指针向左移动直到数值变化。
# 若大于0，右指针向左移动直到数值变化。
# 若小于0，左指针向右移动直到数值变化。
# 直到左右相遇，i++，直到i对应的值大于0.
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()#从小到大排序
        for i in range(n-2):
            if nums[i] > 0:
                return res
            if i >= 1 and nums[i] == nums[i-1]:#跳过相同的数值
                continue
            left = i + 1
            right = n - 1
            while left < right:#双指针
                num = nums[i] + nums[left] + nums[right]
                if num == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while nums[right] == nums[right-1] and right > left + 1: right -= 1#跳过相同的数值
                    right -= 1
                    while nums[left] == nums[left+1] and right > left + 1: left += 1#跳过相同的数值
                    left += 1
                elif num > 0:
                    while nums[right] == nums[right - 1] and right > left + 1: right -= 1#跳过相同的数值
                    right -= 1
                else:
                    while nums[left] == nums[left + 1] and right > left + 1: left += 1#跳过相同的数值
                    left += 1
        return res

s = Solution()
print(s.threeSum([1,2,3,-1,1,-2,-3,0]))