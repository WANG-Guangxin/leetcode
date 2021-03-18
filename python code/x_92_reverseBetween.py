92. 反转链表 II

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
通过次数115,799提交次数219,407

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    	'''
    	其实不难 不要返回 head 因为 head 的位置改变了
    	'''
        r = ListNode()
        r.next = head
        h = r
        for _ in range(left - 1):
            h = h.next
        p = h.next
        for _ in range(right - left):
            q = p.next
            p.next = p.next.next
            q.next = h.next
            h.next = q
        return r.next