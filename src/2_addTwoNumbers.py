'''
2. 两数相加

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。



示例 1：

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]



提示：

    每个链表中的节点数在范围 [1, 100] 内
    0 <= Node.val <= 9
    题目数据保证列表表示的数字不含前导零
'''
# 思路一：
# 先算个位，然后再算十位，依此类推
'''
执行结果：通过
执行用时：48 ms, 在所有 Python3 提交中击败了98.99% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了65.88% 的用户
通过测试用例：1568 / 1568'''
# Definition for singly-linked list.
from typing import Optional
# 注意：提交代码的时候，不能将ListNode的定义也提交！！！
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        end = res
        add = 0#进位
        while l1 or l2 or add:
            # 最多只会进一位！
            if l1 and l2:
                num = l1.val + l2.val + add  # 当前位加和
            elif l1:
                num = l1.val + add  # 当前位加和
            elif l2:
                num = l2.val + add  # 当前位加和
            else:
                num = add
            end.val = num % 10  # 当前位加和余数
            if num // 10:
                add = 1
            else:
                add = 0
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None
            if l1 or l2 or add:
                end.next = ListNode()
                end = end.next
        return res


def get_listnode(num):
    lis = ListNode()
    end = lis
    while num:
        end.val = num % 10
        num = num // 10
        if num:
            end.next = ListNode()
            end = end.next
    return lis

def print_node(lis):
    while lis:
        print(lis.val, end=' ')
        lis = lis.next if lis and lis.next else None
    print()

s = Solution()
def func(num1, num2):
    l1 = get_listnode(num1)
    l2 = get_listnode(num2)
    print_node(l1)
    print_node(l2)
    res = s.addTwoNumbers(l1, l2)
    print_node(res)
    add = 0
    num = 0
    while res:
        num += res.val*10**add
        res = res.next if res and res.next else None
        add += 1
    return num

def list_to_num(lis):
    num = 0
    for i, w in enumerate(lis):
        num += w*10**i
    return num


print(func(list_to_num([0,8,6,5,6,8,3,5]), list_to_num([0])))