485. 最大连续1的个数

给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = r = ans = 0
        while r < len(nums):
            if nums[r] == 0:
                ans = max(ans,r-l)
                l = r + 1
            r += 1

        return max(ans,r-l)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        题解
        '''
        maxCount = count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        
        maxCount = max(maxCount, count)
        return maxCount
