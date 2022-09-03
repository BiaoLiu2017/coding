'''
28. 实现 strStr()

实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。



示例 1：

输入：haystack = "hello", needle = "ll"
输出：2

示例 2：

输入：haystack = "aaaaa", needle = "bba"
输出：-1



提示：

    1 <= haystack.length, needle.length <= 104
    haystack 和 needle 仅由小写英文字符组成

'''
# 题目就是实现find()
# 思路一：直接遍历，直到找到符合的。
'''
执行结果：通过
一次性通过！
执行用时：32 ms, 在所有 Python3 提交中击败了89.98% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.90% 的用户
通过测试用例：79 / 79'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

# # 思路二：
# # 直接用find()，内存会少，但实际不会少。
# '''
# 执行结果：通过
# 执行用时：32 ms, 在所有 Python3 提交中击败了89.98% 的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了76.16% 的用户
# 通过测试用例：79 / 79'''
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)

s = Solution()
print(s.strStr('hello', '11'))