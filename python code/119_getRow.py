119. 杨辉三角 II


给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:return [1]
        if rowIndex == 1:return [1,1]
        def Cnk(n,k):
            fenmu = 1
            for i in range(1,k+1):
                fenmu *= i
            fenzi = 1
            for i in range(n,n-k,-1):
                fenzi *= i
            return fenzi/fenmu
        
        ans = [0] * (rowIndex+1)
        for i in range(rowIndex+1):
            ans[i] = int(Cnk(rowIndex,i))
        return ans

