1438. 绝对差不超过限制的最长连续子数组

给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。

 

示例 1：

输入：nums = [8,2,4,7], limit = 4
输出：2 
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4. 
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4. 
因此，满足题意的最长子数组的长度为 2 。
示例 2：

输入：nums = [10,1,2,4,7,2], limit = 5
输出：4 
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
示例 3：

输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3
 

提示：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        肯定超时
        '''
        n = len(nums)
        right,left,ans = 0,0,0
        while right < n:
            tmp = nums[left:right+1]
            Max = max(tmp)
            Min = min(tmp)
            if Max - Min > limit:
                ans = max(ans,right-left)
                left += 1
            right += 1
        return max(ans,right-left)


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        用数据结构 方便查找最大值最小值
        这算水平高吗 直接用个库而已 就是考的了不了解吧
        '''
        from sortedcontainers import SortedList
        s = SortedList()
        left, right = 0, 0
        res = 0
        while right < len(nums):
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


def longestSubarray(self, nums, limit):
    """
    用队列存储滑动窗口的值 方便找最大值最小值
    """    
    r = l = res = 0
    min_q = collections.deque()
    max_q = collections.deque()
    for num in nums:
        while len(min_q) and num < min_q[-1]: min_q.pop()
        while len(max_q) and num > max_q[-1]: max_q.pop()
        min_q.append(num)
        max_q.append(num)
        r += 1;
        while max_q[0] - min_q[0] > limit:
            if min_q[0] == nums[l]: min_q.popleft() 
            if max_q[0] == nums[l]: max_q.popleft()
            l += 1
        res = max(res, r - l)
    return res

