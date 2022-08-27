'''
9. 回文数

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    例如，121 是回文，而 123 不是。



示例 1：

输入：x = 121
输出：true

示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。



提示：

    -231 <= x <= 231 - 1



进阶：你能不将整数转为字符串来解决这个问题吗？

'''
# 思路一：
# 最简单的思路是，先转换为字符串，颠倒，然后再转换为数字，复杂度为O(n)，而且一定会执行n次
'''
执行结果：通过
执行用时：60 ms, 在所有 Python3 提交中击败了77.31% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了7.76% 的用户
通过测试用例：11510 / 11510'''
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_str = str(x)
#         x_reversed = ''
#         for i in range(len(x_str)):#倒序
#             x_reversed += x_str[len(x_str)-i-1]
#         x_reversed = int(x_reversed.rstrip('-'))#注意将最右边的-去掉，不然int()会报错
#         if x_reversed == x:
#             return True
#         else:
#             return False


# 思路二：
# 最简单的思路是，先转换为字符串，然后直接i和length-1-i来判断是否相等；复杂度还是O(n)，但是实际执行小于等于n/2次，并且没有x_reversed，所以也省内存;
# 另外负数和0直接可判断
# 但是很奇怪，速度和内存并没有明显变化
'''
执行结果：通过
执行用时：56 ms, 在所有 Python3 提交中击败了88.50% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了45.77% 的用户
通过测试用例：11510 / 11510
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            x_str = str(x)
            for i in range(int(len(x_str)/2)):
                if x_str[i] == x_str[len(x_str)-1-i]:
                    continue
                else:
                    return False
            return True


# 思路三：
# 显然，思路二是转换字符串最快的算法了，只能不转字符串
# 所以通过除以1/10/100来取余得到每个位数的数字
'''
执行结果：通过
执行用时：76 ms, 在所有 Python3 提交中击败了22.83% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.12% 的用户
通过测试用例：11510 / 11510
'''
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         elif x < 10:
#             return True
#         elif x % 10 == 0:
#             return False
#         else:
#             num_list = []
#             while x:
#                 num_list.append(x % 10)
#                 x = x//10
#             for i in range(len(num_list)):
#                 if num_list[i] == num_list[len(num_list)-1-i]:
#                     continue
#                 else:
#                     return False
#             return True

# 思路四：
# 直接转字符串，然后利用[::-1]倒转
'''
执行结果：通过
执行用时：48 ms, 在所有 Python3 提交中击败了98.19% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了16.56% 的用户
通过测试用例：11510 / 11510'''
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         elif x < 10:
#             return True
#         elif x % 10 == 0:
#             return False
#         else:
#             x = str(x)
#             x_reversed = x[::-1]
#             if x == x_reversed:
#                 return True
#             else:
#                 return False

s =Solution()
s.isPalindrome(121)


