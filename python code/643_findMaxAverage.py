子数组最大平均数 I

给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

 

示例：

输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 

提示：

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r,res = 0,k,0

        ret = [0] * (len(nums) - k + 1) # 不需要维护数组的  这样空间复杂度是O(n)了

        for i in range(k):
            res += nums[i]
        ret[0] = res
        while r < len(nums) :
            ret[l+1] = ret[l] - nums[l] + nums[r]
            r += 1
            l += 1
        return max(ret)/k


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        官方题解
        '''
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)
        
        return maxTotal / k

