697. 数组的度

给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

 

示例 1：

输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2：

输入：[1,2,2,3,1,4,2]
输出：6
 

提示：

nums.length 在1到 50,000 区间范围内。
nums[i] 是一个在 0 到 49,999 范围内的整数。

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        '''
        超级超级慢  
        参考下面的 多用几个字典去记录 不用循环找
        '''
        n = len(nums)
        tmp = collections.defaultdict(int)
        for x in nums:
            tmp[x] += 1
        count = max(tmp.values())
        tmp2 = []
        for ind,val in tmp.items():
            if val == count:
                tmp2.append(ind)
        ans = n
        for ind in tmp2:
            left,right = 0,n-1
            while nums[left] != ind:
                left += 1
            while nums[right] != ind:
                right -= 1
            ans = min(ans,right-left+1)
        return ans








class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right = dict(), dict()
        counter = collections.Counter()
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            counter[num] += 1
        degree = max(counter.values())
        res = len(nums)
        for k, v in counter.items():
            if v == degree:
                res = min(res, right[k] - left[k] + 1)
        return res

