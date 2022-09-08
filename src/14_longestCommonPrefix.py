'''
14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
'''
from typing  import List
# 思路一：
# 先找到最短的字符串，如果为空，返回空，如果非空，则从短到长，判断子串是否在每个字符串中；
# 速度极快，但内存占用大
'''
执行结果：通过
执行用时：28 ms, 在所有 Python3 提交中击败了98.46% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.35% 的用户
通过测试用例：124 / 124'''
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ''
#         shortest = strs[0]
#         for w in strs[1:]:
#             if len(w) < len(shortest):
#                 shortest = w
#         if not shortest:
#             return ''
#         prefix = ''
#         for i in range(1, len(shortest)+1):
#             sub_str = shortest[:i]
#             flag = True
#             for word in strs:
#                 if sub_str == word[:i]:
#                     continue
#                 else:
#                     flag = False
#                     break
#             if not flag:
#                 if i > 1:
#                     prefix = shortest[:i-1]
#                 break
#             else:
#                 prefix = sub_str
#         return prefix

# 思路二：构建字典树
# 构建完字典树之后，直接走字典树来得到最长公共子串
'''
执行结果：通过
执行用时：28 ms, 在所有 Python3 提交中击败了98.46% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了11.57% 的用户
通过测试用例：124 / 124'''
class Trietree:
    def __init__(self):
        self._root = dict()
        self.is_word = False

    def insert_word(self, word):
        cls = self
        for w in word:
            if w not in cls._root:
                cls._root[w] = Trietree()
            cls = cls._root[w]
        cls.is_word = True

    def insert_words(self, words):
        for word in words:
            self.insert_word(word)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        for word in strs:
            if not word:
                return ''
        trie_tree = Trietree()
        trie_tree.insert_words(strs)
        cls = trie_tree
        prefix = ''
        while cls._root:
            keys = list(cls._root.keys())
            if len(keys) > 1:
                break
            elif cls._root[keys[0]].is_word:
                prefix += keys[0]
                break
            else:
                prefix += keys[0]
                cls = cls._root[keys[0]]
        return prefix



s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))


