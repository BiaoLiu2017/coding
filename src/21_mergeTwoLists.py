'''
21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：

输入：l1 = [], l2 = []
输出：[]

示例 3：

输入：l1 = [], l2 = [0]
输出：[0]



提示：

    两个链表的节点数目范围是 [0, 50]
    -100 <= Node.val <= 100
    l1 和 l2 均按 非递减顺序 排列


'''
# 思路1：依次判断两个链表最小值，放置最小值到新链表，直到结束；（迭代）
'''
一次性通过！
执行结果：通过
执行用时：32 ms, 在所有 Python3 提交中击败了97.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了37.17% 的用户
通过测试用例：208 / 208
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#         if list1.val >= list2.val:
#             new_list = list2
#             end = list2
#             list2 = list2.next
#         else:
#             new_list = list1
#             end = list1
#             list1 = list1.next
#         while list1 and list2:
#             if list1.val >= list2.val:
#                 end.next = list2
#                 end = list2
#                 list2 = list2.next
#             else:
#                 end.next = list1
#                 end = list1
#                 list1 = list1.next
#         if list1:
#             end.next = list1
#         if list2:
#             end.next = list2
#         return new_list


# 思路二，利用递归；
'''
执行结果：通过
执行用时：36 ms, 在所有 Python3 提交中击败了88.17% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.72% 的用户
通过测试用例：208 / 208'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 每次取最小的出来，剩余的继续merge；
        # 基线条件：
        if not list1:
            return list2
        if not list2:
            return list1
        # 递归条件：
        if list1.val >= list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1




def generate_linked_list(lis):
    # 用于从list来生成对应的链表
    if not lis:
        return None
    else:
        node = ListNode(lis[0])
        linked_list = node
        end = node
        for i in lis[1:]:
            node = ListNode(i)
            end.next = node
            end = node
        return linked_list



s = Solution()
list1 = generate_linked_list([1,2,4])
list2 = generate_linked_list([1,2,3,4,5])
new_list = s.mergeTwoLists(list1, list2)
while new_list:
    print(new_list.val)
    new_list = new_list.next
