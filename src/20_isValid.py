'''
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。



示例 1：

输入：s = "()"
输出：true

示例 2：

输入：s = "()[]{}"
输出：true

示例 3：

输入：s = "(]"
输出：false

示例 4：

输入：s = "([)]"
输出：false

示例 5：

输入：s = "{[]}"
输出：true



提示：

    1 <= s.length <= 104
    s 仅由括号 '()[]{}' 组成

'''
# 假设三种符号分别用x,y,z表示
# 思路一：
# 原本的思路：满足四点即可：1.左x右边要么是右x，要么是左y/z；2.左x/y/z右x/y/z数量一样；但是发现并不满足少见情况：如[([]])；
# 因此思路为：从左到右扫列表，如果找到扫到“中心”（即[]或()或{}）就去掉中心两侧对称的字符，然后找下一个中心，迭代直到结束；
# 虽然最后通过了，但是由于完全靠穷尽所有可能性，代码成本高，容易出错，所以不算好代码；
'''
执行结果：通过
执行用时：36 ms, 在所有 Python3 提交中击败了76.32% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了14.72% 的用户
通过测试用例：92 / 92'''
# class Solution:
#     def isValid(self, s: str) -> bool:
#         map_dict = {'(': ')', '[': ']', '{': '}'}
#         if len(s) % 2 !=0 :
#             return False
#         elif not s:
#             return True
#         else:
#             start_index = 0
#             while s:
#                 length = len(s)
#                 if start_index >= length - 1:
#                     return False
#                 for i in range(start_index, length - 1):
#                     if s[i] in map_dict and map_dict[s[i]] == s[i+1]:#找到中心
#                         if i > 0:#即左边还有字符
#                             for move_step in range(1, i+1):
#                                 left_index = i - move_step
#                                 right_index = i + 1 + move_step
#                                 if right_index < length and s[left_index] in map_dict and map_dict[s[left_index]] == s[right_index]:
#                                     if move_step == i:#即去除最左边
#                                         start_index = left_index
#                                         s = s[right_index+1:]
#                                         break
#                                     elif right_index == length - 1:#即去除最右边
#                                         start_index = left_index
#                                         s = s[:left_index]
#                                         break
#                                     else:
#                                         continue
#                                 else:
#                                     start_index = left_index + 1
#                                     s = s[:left_index + 1] + s[right_index:]
#                                     break
#                         else:
#                             s = s[2:]#左边无字符，直接去除
#                         break
#                     elif i == length - 2:#找到最后都没有center
#                         return False
#             return True#所有字符都去掉了，说明符合


# 思路二：利用栈
# 遇到左括号就进栈push，遇到右括号并且栈顶为与之对应的左括号，就把栈顶元素出栈。最后看栈里面还有没有其他元素，如果为空，即匹配。
# 需要注意，空字符串是满足括号匹配的，即输出 true。
'''
执行结果：通过
执行用时：32 ms, 在所有 Python3 提交中击败了91.63% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了62.68% 的用户
通过测试用例：92 / 92'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        else:
            left_char_set = {'(', '[', '{'}
            map_dict = {'(': ')', '[': ']', '{': '}'}
            char_list = []#用列表来实现栈
            length = len(s)
            for i in range(length):
                if s[i] in left_char_set:
                    char_list.append(s[i])
                else:
                    if char_list and map_dict[char_list[-1]] == s[i]:
                        # 栈内有元素，并且匹配，出栈
                        char_list.pop()
                    else:
                        return False
            if not char_list:
                return True
            else:
                return False

s = Solution()
print(s.isValid("[[[]"))




