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
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         for i in range(0, len(haystack) - len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i
#         return -1

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


# 思路三：构建Trie Tree，然后搜索，只需要前缀匹配即可，不是标准的trie tree
'''
执行结果：通过
执行用时：240 ms, 在所有 Python3 提交中击败了6.66% 的用户
内存消耗：21.8 MB, 在所有 Python3 提交中击败了5.29% 的用户
通过测试用例：79 / 79'''
# class TrieTree:
#     # 构建Trie Tree
#     def __init__(self):
#         self._root = dict()
#         self._index = None
#
#     def insert_word(self, word, index):
#         cls = self
#         for w in word:
#             if w not in cls._root:
#                 cls._root[w] = TrieTree()
#             cls = cls._root[w]
#             if cls._index == None:
#                 cls._index = index#每个前缀字符串都对应一个index
#
#     def insert_words(self, word_list, index_list):
#         for word, index in zip(word_list, index_list):
#             self.insert_word(word, index)
#
#
# class SearchTireTree:
#     def __init__(self, word_list, index_list):
#         # 构建trie tree
#         self.trie_tree = TrieTree()
#         self.trie_tree.insert_words(word_list, index_list)
#
#     def search(self, word):
#         # 前缀搜索
#         cls = self.trie_tree
#         for w in word:
#             if w not in cls._root:
#                 return False
#             else:
#                 cls = cls._root[w]
#         return cls._index
#
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         word_list = []
#         index_list = []
#         for i in range(len(haystack)):
#             word_list.append(haystack[i:])
#             index_list.append(i)
#         search_trie_tree = SearchTireTree(word_list, index_list)#构建trie tree
#         res = search_trie_tree.search(needle)
#         if not str(res).isnumeric():#0==False为True
#             return -1
#         else:
#             return res

# 思路四：KMP算法(自己写的，很垃圾)
'''
执行结果：通过
执行用时：44 ms, 在所有 Python3 提交中击败了15.69% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了48.18% 的用户
通过测试用例：79 / 79'''
# def get_prefix(sentence):
#     # 获取前缀集合
#     return set([sentence[:i] for i in range(1, len(sentence))])
#
# def get_postfix(sentence):
#     # 获取后缀集合
#     return set([sentence[-i:] for i in range(1, len(sentence))])
#
# def get_max_length(common_fix):
#     length = len(common_fix[0])
#     for w in common_fix[1:]:
#         if len(w) > length:
#             length = len(w)
#     return length
#
# def get_partial_match_table(sentence):
#     # 得到部分匹配表，用于指导index往后移动
#     table = []
#     for i in range(len(sentence)):
#         now_sentence = sentence[:i + 1]
#         prefix = get_prefix(now_sentence)
#         postfix = get_postfix(now_sentence)
#         common_fix = list(prefix.intersection(postfix))
#         if common_fix:
#             table.append(get_max_length(common_fix))
#         else:
#             table.append(0)
#     return table
#
# def get_matched_length(sentence, start_index, word):
#     # 获取当前匹配长度
#     word_length = len(word)
#     for length in range(word_length - 1, 0, -1):
#         # print(length)
#         if word[:length] == sentence[start_index:start_index + length]:
#             return length
#     return 0
#
# def kmp_match(sentence, word):
#     # kmp算法进行字符串匹配
#     start_index = 0
#     word_length = len(word)
#     partial_match_table = get_partial_match_table(word)
#     # print(partial_match_table)
#     while start_index < len(sentence):
#         if sentence[start_index:start_index + word_length] == word:
#             return start_index
#         else:
#             matched_length = get_matched_length(sentence, start_index, word)
#             if matched_length:
#                 start_index += (matched_length - partial_match_table[matched_length - 1])
#             else:
#                 start_index += 1
#     return -1
#
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return kmp_match(haystack, needle)


# 思路五：KMP算法
'''
执行结果：通过
执行用时：32 ms, 在所有 Python3 提交中击败了90.04% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了74.50% 的用户
通过测试用例：79 / 79'''
def get_partial_match_table(p):
    # 依次获取每个位置的next值
    # input: ababacd
    # [0, 0, 1, 2, 3, 0, 0]
    nxt = [0]
    x = 1
    now = 0
    while x < len(p):
        if p[now] == p[x]:
            nxt.append(now+1)
            now += 1
            x += 1
        elif now:
            now = nxt[now-1]
        else:
            nxt.append(0)
            x += 1
    return nxt

def search(s, p):
    nxt = get_partial_match_table(p)
    tar = 0#主串中将要匹配的位置
    pos = 0#模式串中将要匹配的位置
    while tar < len(s):
        if s[tar] == p[pos]:
            tar += 1
            pos += 1
        elif pos:
            pos = nxt[pos-1]
        else:
            tar += 1
        if pos == len(p):
            return tar-len(p)
    return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return search(haystack, needle)

s = Solution()
print(s.strStr("ababcababac", "ababa"))