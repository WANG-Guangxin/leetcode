82. 删除排序链表中的重复元素 II

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        hashmap = collections.defaultdict(list)
        h = ListNode()
        h.next = head
        p = h
        while p.next:
            hashmap[p.next.val].append(1)
            p = p.next
        p = h
        while p.next:
            if len(hashmap[p.next.val]) > 1:
                p.next = p.next.next
            else:
                p = p.next
        return h.next
