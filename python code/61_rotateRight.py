61. 旋转链表

给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]
 

提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:return head
        h = ListNode()
        h.next = head
        p = pre = h
        i = 0
        while p.next and i < k:
            p = p.next
            i += 1
        if not p.next:
            if i < k: 
                k %= i
                for j in range(i-k):
                    pre = pre.next
                p = pre
                while p.next:
                    p = p.next
            if i == k: return h.next
        else:
            while p.next:
                pre = pre.next
                p = p.next
        p.next = h.next
        h.next = pre.next
        pre.next = None
        return h.next